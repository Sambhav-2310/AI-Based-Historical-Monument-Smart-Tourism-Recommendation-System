import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# ============================================================
# 1. DATA LOADING & PREPROCESSING
# ============================================================

def load_monuments_data():
    """
    Load monument data from CSV file.
    
    Returns:
        DataFrame: Monuments data with all features
    """
    csv_path = os.path.join(os.path.dirname(__file__), 'monuments.csv')
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"monuments.csv not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    
    # Clean and standardize data
    df['monument_name'] = df['monument_name'].str.strip()
    df['city'] = df['city'].str.strip().str.lower()
    df['state'] = df['state'].str.strip().str.lower()
    df['category'] = df['category'].str.strip().str.lower()
    df['budget'] = df['budget'].str.strip().str.lower()
    df['crowd_level'] = df['crowd_level'].str.strip().str.lower()
    df['best_season'] = df['best_season'].str.strip().str.lower()
    df['weather_type'] = df['weather_type'].str.strip().str.lower()
    
    print(f"[SUCCESS] Loaded {len(df)} monuments from database")
    return df


def create_feature_vector(row):
    """
    Combine relevant features into a single text vector for TF-IDF processing.
    
    Args:
        row: A single monument record from DataFrame
    
    Returns:
        str: Combined text representation of monument features
    """
    features = [
        str(row['monument_name']),
        row['category'],
        row['city'],
        row['state'],
        row['budget'],
        row['crowd_level'],
        row['best_season'],
        row['weather_type'],
        str(row['description'])
    ]
    
    # Join features with spaces for vectorization
    combined_text = ' '.join(features)
    return combined_text


def preprocess_monuments(df):
    """
    Preprocess monument data for ML model.
    
    Args:
        df: Raw monuments DataFrame
    
    Returns:
        DataFrame: Processed monuments data with feature vectors
    """
    # Create combined feature vectors
    df['feature_vector'] = df.apply(create_feature_vector, axis=1)
    
    print("[SUCCESS] Feature vectors created")
    return df


# ============================================================
# 2. VECTORIZATION & SIMILARITY COMPUTATION
# ============================================================

def create_user_preference_vector(user_prefs):
    """
    Create a text vector from user preferences.
    
    Args:
        user_prefs (dict): User preference dictionary with keys:
                          - category
                          - budget
                          - state_city
                          - duration
                          - season
                          - crowd
                          - weather
    
    Returns:
        str: Combined text representation of user preferences
    """
    prefs_list = [
        user_prefs.get('category', '').lower(),
        user_prefs.get('budget', '').lower(),
        user_prefs.get('state_city', '').lower(),
        user_prefs.get('season', '').lower(),
        user_prefs.get('crowd', '').lower(),
        user_prefs.get('weather', '').lower()
    ]
    
    # Filter out empty strings and join
    prefs_text = ' '.join([p for p in prefs_list if p])
    return prefs_text


def compute_similarity_scores(monument_vectors, user_vector):
    """
    Compute cosine similarity scores between user preferences and monuments.
    
    Args:
        monument_vectors: TF-IDF vectors of monuments
        user_vector: TF-IDF vector of user preferences
    
    Returns:
        ndarray: Similarity scores for each monument
    """
    # Compute cosine similarity
    similarities = cosine_similarity(user_vector, monument_vectors)[0]
    
    print(f"[SUCCESS] Computed similarity scores for all monuments")
    return similarities


# ============================================================
# 3. FILTERING & RANKING
# ============================================================

def apply_category_filter(df, category):
    """
    Filter monuments by historical category.
    
    Args:
        df: Monuments DataFrame
        category: User's preferred category
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not category or category.lower() == 'any':
        return df
    
    category_lower = category.lower()
    filtered = df[df['category'].str.contains(category_lower, case=False, na=False)]
    
    return filtered if len(filtered) > 0 else df


def apply_budget_filter(df, budget):
    """
    Filter monuments by budget suitability.
    
    Args:
        df: Monuments DataFrame
        budget: User's budget preference (Low, Moderate, etc.)
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not budget or budget.lower() == 'any':
        return df
    
    budget_lower = budget.lower()
    filtered = df[df['budget'].str.lower() == budget_lower]
    
    return filtered if len(filtered) > 0 else df


def apply_location_filter(df, state_city):
    """
    Filter monuments by state or city.
    
    Args:
        df: Monuments DataFrame
        state_city: User's preferred state or city
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not state_city or state_city.lower() == 'any':
        return df
    
    location_lower = state_city.lower()
    filtered = df[
        (df['state'].str.lower().str.contains(location_lower, na=False)) |
        (df['city'].str.lower().str.contains(location_lower, na=False))
    ]
    
    return filtered if len(filtered) > 0 else df


def apply_season_filter(df, season):
    """
    Filter monuments by best visiting season.
    
    Args:
        df: Monuments DataFrame
        season: User's preferred season
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not season or season.lower() == 'any':
        return df
    
    season_lower = season.lower()
    filtered = df[df['best_season'].str.lower().str.contains(season_lower, na=False)]
    
    return filtered if len(filtered) > 0 else df


def apply_crowd_filter(df, crowd):
    """
    Filter monuments by crowd level preference.
    
    Args:
        df: Monuments DataFrame
        crowd: User's crowd preference (Low, High, etc.)
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not crowd or crowd.lower() == 'any':
        return df
    
    crowd_lower = crowd.lower()
    
    # Map preferences to crowd levels
    if crowd_lower in ['low', 'quiet']:
        filtered = df[df['crowd_level'].str.lower().isin(['low', 'moderate'])]
    elif crowd_lower in ['high', 'busy']:
        filtered = df[~df['crowd_level'].str.lower().isin(['low'])]
    else:
        filtered = df[df['crowd_level'].str.lower().str.contains(crowd_lower, na=False)]
    
    return filtered if len(filtered) > 0 else df


def apply_weather_filter(df, weather):
    """
    Filter monuments by weather type preference.
    
    Args:
        df: Monuments DataFrame
        weather: User's weather preference
    
    Returns:
        DataFrame: Filtered monuments
    """
    if not weather or weather.lower() == 'any':
        return df
    
    weather_lower = weather.lower()
    filtered = df[df['weather_type'].str.lower().str.contains(weather_lower, na=False)]
    
    return filtered if len(filtered) > 0 else df


def apply_all_filters(df, user_prefs):
    """
    Apply all preference filters intelligently.
    If all monuments are filtered out, return all monuments.
    
    Args:
        df: Monuments DataFrame
        user_prefs (dict): User preference dictionary
    
    Returns:
        DataFrame: Filtered monuments (or full df if all filtered out)
    """
    filtered_df = df.copy()
    
    # Apply filters in order
    filtered_df = apply_category_filter(filtered_df, user_prefs.get('category', ''))
    filtered_df = apply_budget_filter(filtered_df, user_prefs.get('budget', ''))
    filtered_df = apply_location_filter(filtered_df, user_prefs.get('state_city', ''))
    filtered_df = apply_season_filter(filtered_df, user_prefs.get('season', ''))
    filtered_df = apply_crowd_filter(filtered_df, user_prefs.get('crowd', ''))
    filtered_df = apply_weather_filter(filtered_df, user_prefs.get('weather', ''))
    
    # If filtering removed all monuments, use all monuments
    if len(filtered_df) == 0:
        print("[WARNING] All monuments filtered out. Using all monuments for matching...")
        filtered_df = df.copy()
    
    print(f"[FILTER] Filters applied: {len(filtered_df)} monuments remain")
    
    return filtered_df


# ============================================================
# 4. MAIN RECOMMENDATION ENGINE
# ============================================================

def get_recommendations(user_preferences, num_recommendations=5):
    """
    Main function: Get monument recommendations based on user preferences.
    
    This function:
    1. Loads and preprocesses monument data
    2. Vectorizes monuments using TF-IDF
    3. Creates user preference vector
    4. Computes similarity scores
    5. Filters by user preferences
    6. Returns top recommendations
    
    Args:
        user_preferences (dict): Dictionary containing:
            - category: Historical category (Temple, Fort, etc.)
            - budget: Budget level (Low, Moderate, High)
            - state_city: Preferred state or city
            - duration: Travel duration (not used for filtering, just for info)
            - season: Preferred season
            - crowd: Crowd preference
            - weather: Weather preference
        num_recommendations (int): Number of recommendations to return (default: 5)
    
    Returns:
        list: List of recommend monuments with details
              Each item is a dictionary containing:
              {
                  'monument': name,
                  'city': city,
                  'state': state,
                  'category': category,
                  'budget': budget,
                  'season': best_season,
                  'crowd_level': crowd_level,
                  'weather': weather_type,
                  'rating': rating,
                  'description': description,
                  'match_score': similarity_score (0-100)
              }
    """
    
    try:
        # Step 1: Load and preprocess data
        print("\n[DATA] Loading monument database...")
        monuments_df = load_monuments_data()
        monuments_df = preprocess_monuments(monuments_df)
        print(f"[DATA] Loaded {len(monuments_df)} monuments")
        
        # Step 2: Apply user preference filters
        print(f"\n[FILTER] Applying filters with preferences: {user_preferences}")
        filtered_df = apply_all_filters(monuments_df, user_preferences)
        
        # If no monuments match after filtering, use all monuments
        if len(filtered_df) == 0:
            print("[WARNING] No exact matches found. Using all monuments for recommendation...")
            filtered_df = monuments_df.copy()
        
        # Step 3: Vectorize using TF-IDF
        print("\n[VECTORIZE] Vectorizing data...")
        vectorizer = TfidfVectorizer(
            max_features=100,
            stop_words='english',
            lowercase=True
        )
        
        # Fit on all monuments and transform
        monument_vectors = vectorizer.fit_transform(monuments_df['feature_vector'])
        
        # Create user preference vector
        user_pref_text = create_user_preference_vector(user_preferences)
        user_vector = vectorizer.transform([user_pref_text])
        
        # Step 4: Compute similarity scores
        print("\n[SIMILARITY] Computing similarity scores...")
        similarities = compute_similarity_scores(monument_vectors, user_vector)
        
        # Add similarity scores to filtered dataframe
        filtered_df = filtered_df.copy()
        filtered_indices = filtered_df.index
        filtered_df['similarity_score'] = similarities[filtered_indices]
        
        # Step 5: Rank and sort by similarity
        recommendations_df = filtered_df.sort_values('similarity_score', ascending=False)
        
        # Step 6: Return top N recommendations
        top_recommendations_df = recommendations_df.head(num_recommendations)
        
        # Format recommendations
        recommendations = []
        for _, row in top_recommendations_df.iterrows():
            recommendation = {
                'monument': row['monument_name'],
                'city': row['city'].title(),
                'state': row['state'].title(),
                'category': row['category'].title(),
                'budget': row['budget'].title(),
                'season': row['best_season'],
                'crowd_level': row['crowd_level'].title(),
                'weather': row['weather_type'].title(),
                'rating': row['rating'],
                'description': row['description'],
                'match_score': round(row['similarity_score'] * 100, 1)
            }
            recommendations.append(recommendation)
        
        print(f"\n[SUCCESS] Generated {len(recommendations)} recommendations")
        return recommendations
    
    except Exception as e:
        print(f"[ERROR] Error in recommendation engine: {str(e)}")
        return []


# ============================================================
# 5. UTILITY FUNCTIONS
# ============================================================

def get_all_categories():
    """Get list of all available monument categories."""
    try:
        df = load_monuments_data()
        categories = sorted(df['category'].unique().tolist())
        return categories
    except:
        return []


def get_all_states():
    """Get list of all available states."""
    try:
        df = load_monuments_data()
        states = sorted(df['state'].unique().tolist())
        return states
    except:
        return []


def get_all_seasons():
    """Get list of all available seasons."""
    try:
        df = load_monuments_data()
        seasons = set()
        for season_str in df['best_season'].unique():
            season_parts = [s.strip() for s in season_str.split(',')]
            seasons.update(season_parts)
        return sorted(seasons)
    except:
        return []


# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":
    """
    Example usage of the recommendation engine.
    """
    
    # Sample user preferences
    sample_user_prefs = {
        'category': 'Temple',
        'budget': 'Moderate',
        'state_city': 'Rajasthan',
        'duration': '3 days',
        'season': 'October',
        'crowd': 'Moderate',
        'weather': 'Moderate'
    }
    
    # Get recommendations
    recommendations = get_recommendations(sample_user_prefs, num_recommendations=5)
    
    # Display results
    print("\n" + "="*80)
    print("RECOMMENDED MONUMENTS")
    print("="*80 + "\n")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['monument']} ({rec['rating']}⭐)")
        print(f"   Location: {rec['city']}, {rec['state']}")
        print(f"   Category: {rec['category']}")
        print(f"   Budget: {rec['budget']} | Season: {rec['season']} | Weather: {rec['weather']}")
        print(f"   Crowd Level: {rec['crowd_level']} | Match Score: {rec['match_score']}%")
        print(f"   Description: {rec['description']}")
        print()
