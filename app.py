"""
Heritage AI - Flask Backend Application
=========================================
A Flask-based web application for AI-powered heritage tourist recommendations.

This application:
1. Serves the frontend pages (HTML/CSS)
2. Handles user form submissions
3. Runs the ML recommendation engine
4. Returns personalized monument recommendations

Routes:
- GET  /                    - Home page
- GET  /form               - Recommendation form
- GET  /about              - About the project
- GET  /results            - Results page (displays recommendations)
- POST /api/get-recommendations - API endpoint for ML recommendations
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from recommendation import get_recommendations
import os


# ============================================================
# FLASK APP INITIALIZATION
# ============================================================

app = Flask(
    __name__,
    template_folder='Frontend/templates',
    static_folder='Frontend/static'
)


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors gracefully."""
    return render_template('index.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors gracefully."""
    return jsonify({'error': 'Internal server error'}), 500


# ============================================================
# ROUTES - PAGE RENDERING
# ============================================================

@app.route('/')
def home():
    """
    Home Page Route
    
    Displays the main landing page with project information
    and links to other sections.
    
    Returns:
        HTML: Rendered index.html
    """
    return render_template('index.html')


@app.route('/form')
def form():
    """
    Recommendation Form Route
    
    Displays the form where users input their preferences:
    - Historical category
    - Budget
    - Preferred state/city
    - Travel duration
    - Preferred season
    - Crowd preference
    - Weather preference
    
    Returns:
        HTML: Rendered form.html
    """
    return render_template('form.html')


@app.route('/about')
def about():
    """
    About Page Route
    
    Displays information about:
    - Project objective
    - ML integration details
    - Technologies used
    - How the system works
    
    Returns:
        HTML: Rendered about.html
    """
    return render_template('about.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    Results Page Route
    
    GET:  Displays empty results page
    POST: Receives form data, runs ML engine, displays recommendations
    
    Form Parameters (POST):
    - category: Monument historical category
    - budget: Budget level (Low, Moderate, High)
    - state_city: Preferred state or city
    - duration: Travel duration
    - season: Preferred season
    - crowd: Crowd preference
    - weather: Weather preference
    
    Returns:
        HTML: Rendered results.html with recommendations
    """
    recommendations = []
    user_prefs = {}
    error_message = None
    
    if request.method == 'POST':
        try:
            # Step 1: Collect form data
            user_prefs = {
                'category': request.form.get('category', '').strip(),
                'budget': request.form.get('budget', '').strip(),
                'state_city': request.form.get('state_city', '').strip(),
                'duration': request.form.get('duration', '').strip(),
                'season': request.form.get('season', '').strip(),
                'crowd': request.form.get('crowd', '').strip(),
                'weather': request.form.get('weather', '').strip()
            }
            
            # Step 2: Validate that at least one preference is selected
            preferences_filled = any([
                user_prefs['category'],
                user_prefs['budget'],
                user_prefs['state_city'],
                user_prefs['season'],
                user_prefs['crowd'],
                user_prefs['weather']
            ])
            
            if not preferences_filled:
                error_message = "[WARNING] Please select at least one preference to get recommendations."
                return render_template('results.html', 
                                     recommendations=[], 
                                     user_prefs={},
                                     error_message=error_message)
            
            # Step 3: Call ML recommendation engine
            print("\n" + "="*80)
            print(f"Generating recommendations for user preferences:")
            print(f"  Category: {user_prefs['category'] or 'Any'}")
            print(f"  Budget: {user_prefs['budget'] or 'Any'}")
            print(f"  Location: {user_prefs['state_city'] or 'Any'}")
            print(f"  Season: {user_prefs['season'] or 'Any'}")
            print(f"  Crowd: {user_prefs['crowd'] or 'Any'}")
            print(f"  Weather: {user_prefs['weather'] or 'Any'}")
            print("="*80)
            
            recommendations = get_recommendations(user_prefs, num_recommendations=15)
            
            # Step 4: Handle case where no recommendations found
            if not recommendations:
                error_message = "❌ No recommendations found. Please try different preferences."
                return render_template('results.html', 
                                     recommendations=[], 
                                     user_prefs=user_prefs,
                                     error_message=error_message)
            
            print(f"\n✅ Successfully generated {len(recommendations)} recommendations")
            
        except Exception as e:
            error_message = f"❌ Error processing request: {str(e)}"
            print(f"Error: {error_message}")
            return render_template('results.html', 
                                 recommendations=[], 
                                 user_prefs={},
                                 error_message=error_message)
    
    return render_template('results.html', 
                         recommendations=recommendations, 
                         user_prefs=user_prefs,
                         error_message=error_message)


# ============================================================
# API ENDPOINTS (JSON RESPONSES)
# ============================================================

@app.route('/api/get-recommendations', methods=['POST'])
def api_get_recommendations():
    """
    API Endpoint for ML Recommendations
    
    Returns JSON recommendations for API clients.
    
    Request JSON:
    {
        'category': 'Temple',
        'budget': 'Moderate',
        'state_city': 'Rajasthan',
        'duration': '3 days',
        'season': 'October',
        'crowd': 'Moderate',
        'weather': 'Moderate'
    }
    
    Returns:
        JSON: {
            'success': bool,
            'recommendations': [list of monument objects],
            'count': number of recommendations,
            'message': status message
        }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Prepare user preferences
        user_prefs = {
            'category': data.get('category', '').strip(),
            'budget': data.get('budget', '').strip(),
            'state_city': data.get('state_city', '').strip(),
            'duration': data.get('duration', '').strip(),
            'season': data.get('season', '').strip(),
            'crowd': data.get('crowd', '').strip(),
            'weather': data.get('weather', '').strip()
        }
        
        # Get recommendations
        recommendations = get_recommendations(user_prefs, num_recommendations=15)
        
        return jsonify({
            'success': True,
            'recommendations': recommendations,
            'count': len(recommendations),
            'message': f'Successfully generated {len(recommendations)} recommendations'
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500


@app.route('/api/health')
def api_health():
    """
    Health Check Endpoint
    
    Returns:
        JSON: Status information
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Heritage AI Backend is running'
    }), 200


# ============================================================
# STATIC FILES ARE SERVED AUTOMATICALLY BY FLASK
# ============================================================
# No need for custom route - Flask automatically serves files
# from the static_folder defined in app initialization


# ============================================================
# MAIN APPLICATION ENTRY POINT
# ============================================================

if __name__ == '__main__':
    """
    Run the Flask development server.
    
    Configure:
    - debug=True:      Enables auto-reload and better error messages
    - host='0.0.0.0':  Accessible from any IP address
    - port=5000:       Uses port 5000 (change if needed)
    """
    
    print("\n" + "="*80)
    print("[HERITAGE AI - HISTORICAL MONUMENT RECOMMENDATION SYSTEM]")
    print("="*80)
    print("\n[*] Starting Flask server...")
    print("   URL: http://127.0.0.1:5000")
    print("   Home: http://127.0.0.1:5000/")
    print("   Form: http://127.0.0.1:5000/form")
    print("   Results: http://127.0.0.1:5000/results")
    print("   About: http://127.0.0.1:5000/about")
    print("\n[INFO] Press Ctrl+C to stop the server\n")
    print("="*80 + "\n")
    
    # Run Flask development server
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=True
    )
