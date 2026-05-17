# 🏛️ Heritage AI - Setup & Usage Guide

## Project Overview

**Heritage AI** is an AI-powered tourism recommendation system that recommends historical monuments and heritage destinations based on user preferences using machine learning.

**Tech Stack:**
- Backend: Python + Flask
- ML Engine: Scikit-learn (TF-IDF + Cosine Similarity)
- Frontend: HTML + CSS (Already Complete ✓)
- Data: Pandas + NumPy

---

## 📋 Project Structure

```
ML PROJECT/
│
├── app.py                          # Flask backend application
├── recommendation.py               # ML recommendation engine
├── monuments.csv                   # Historical monuments dataset
├── requirements.txt                # Python dependencies
│
├── Frontend/
│   ├── templates/
│   │   ├── index.html             # Home page
│   │   ├── form.html              # Recommendation form
│   │   ├── results.html           # Results/recommendations display
│   │   └── about.html             # Project information
│   │
│   └── static/
│       └── style.css              # All styling
│
└── README.md / SETUP.md           # Documentation (this file)
```

---

## 🚀 Quick Start (5 Steps)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask 2.3.3 - Web framework
- Pandas 2.0.3 - Data manipulation
- NumPy 1.24.3 - Numerical computing
- Scikit-learn 1.3.0 - Machine learning library
- Werkzeug 2.3.7 - Flask utility library

### Step 2: Verify Dataset

Check that `monuments.csv` exists in the project root:

```bash
ls monuments.csv
```

The CSV contains 25 Indian historical monuments with features:
- Monument name, city, state
- Category, budget, season
- Crowd level, weather type
- Rating, description

### Step 3: Start Flask Server

```bash
python app.py
```

**Expected Output:**
```
================================================================================
🏛️  HERITAGE AI - HISTORICAL MONUMENT RECOMMENDATION SYSTEM
================================================================================

📍 Starting Flask server...
   URL: http://127.0.0.1:5000
   Home: http://127.0.0.1:5000/
   Form: http://127.0.0.1:5000/form
   Results: http://127.0.0.1:5000/results
   About: http://127.0.0.1:5000/about

⏸️  Press Ctrl+C to stop the server

================================================================================
```

### Step 4: Open Web Browser

Navigate to: **http://127.0.0.1:5000/**

### Step 5: Get Recommendations

1. Click "Get Recommendation" on home page
2. Fill the form with preferences
3. Click "Submit"
4. View personalized monument recommendations

---

## 📖 How to Use the Application

### Home Page (`/`)
- Landing page with project introduction
- Links to form and about pages
- Project vision

### Recommendation Form (`/form`)
**Form Fields:**

1. **Historical Category**
   - Temple, Fort, UNESCO World Heritage, Monument, etc.
   - Optional: Select "Any" to see all types

2. **Budget**
   - Low, Moderate, High
   - Indicates entrance fee and accessibility

3. **Preferred State/City**
   - Example: Rajasthan, Delhi, Uttar Pradesh, Mumbai
   - Or specific city: Agra, Jaipur, Varanasi

4. **Travel Duration**
   - 1 day, 2-3 days, 4-7 days, 1+ weeks
   - For informational purposes in recommendations

5. **Preferred Season**
   - Summer, Monsoon, Winter, Spring
   - Best visiting season for weather

6. **Crowd Preference**
   - Low (Quiet), Moderate, High (Busy)
   - Preferred crowd intensity

7. **Weather Preference**
   - Hot, Moderate, Humid, Cold
   - Preferred climate conditions

### Results Page (`/results`)
**Displays for each recommendation:**
- Monument name with rating (⭐)
- Location (City, State)
- Category and historical significance
- Budget level
- Best season to visit
- Weather type at destination
- Crowd level expectations
- Match score (0-100%) based on user preferences
- Full description

**Example Output:**
```
1. Taj Mahal (4.8⭐)
   Location: Agra, Uttar Pradesh
   Category: UNESCO World Heritage
   Budget: Moderate | Season: October-March | Weather: Moderate
   Crowd Level: High | Match Score: 94.5%
   Description: An iconic white marble mausoleum built by Mughal 
   Emperor Shah Jahan...
```

### About Page (`/about`)
- Project objective and motivation
- ML integration explanation
- Technologies used
- How the recommendation system works

---

## 🤖 ML Recommendation Engine Explained

### How It Works

#### 1. **Data Preparation**
```python
# Load monuments from CSV
monuments_df = load_monuments_data()  # 25 monuments
```

#### 2. **Feature Combination**
Each monument is represented as combined text:
```
"taj mahal unesco world heritage moderate october-march high moderate..."
```

Features combined:
- Monument name
- Category
- City & State
- Budget level
- Crowd level
- Season
- Weather
- Description

#### 3. **TF-IDF Vectorization**
Convert text to numerical vectors using TF-IDF:
```python
vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
monument_vectors = vectorizer.fit_transform(feature_text)
user_vector = vectorizer.transform(user_preferences_text)
```

**Why TF-IDF?**
- Assigns weights to words based on importance
- Common words get lower weights, specific words get higher weights
- Captures the essence of each monument

#### 4. **Similarity Calculation**
Calculate cosine similarity between user preferences and monuments:
```python
similarities = cosine_similarity(user_vector, monument_vectors)
```

**Output:** Score from 0 to 1 (0-100%)

#### 5. **Filtering**
Apply user preferences as filters:
```
if budget selected:
    keep only monuments matching budget
if season selected:
    keep only monuments with matching season
if category selected:
    keep only monuments in that category
... etc
```

#### 6. **Ranking & Return**
Sort filtered monuments by similarity score (highest first):
```python
recommendations = sorted(filtered_monuments, by='similarity_score')
return top_5_recommendations
```

### Algorithm Flow

```
User Input
    ↓
Load Monuments Data (25 records)
    ↓
Create Feature Vectors (combined text)
    ↓
Apply TF-IDF Vectorization
    ↓
Create User Preference Vector
    ↓
Calculate Cosine Similarity Scores
    ↓
Apply Category/Budget/Location/Season Filters
    ↓
Sort by Similarity Score (Descending)
    ↓
Return Top 5 Recommendations
    ↓
Display Results on Web Page
```

### Why This Approach?

**Advantages:**
- ✓ Simple and interpretable
- ✓ No complex training required
- ✓ Works well with small datasets
- ✓ Fast inference (real-time recommendations)
- ✓ Easy to add new monuments (just add CSV row)

**Trade-offs:**
- × No deep learning (not necessary for this problem)
- × Simple similarity metric (but effective for recommendations)
- × Limited to feature combinations (not user behavior history)

---

## 📁 File Descriptions

### `app.py` (Flask Backend)
```python
@app.route('/')                    # Home page
@app.route('/form')               # Form page
@app.route('/about')              # About page
@app.route('/results', methods=['GET', 'POST'])  # Results & recommendations
@app.route('/api/get-recommendations', methods=['POST'])  # API endpoint
```

**Key Functions:**
- `home()` - Serve home.html
- `form()` - Serve form.html
- `results()` - Handle form submission, call ML engine
- `api_get_recommendations()` - JSON API for recommendations

### `recommendation.py` (ML Engine)
```python
get_recommendations(user_preferences)  # Main function
├── load_monuments_data()              # Load CSV
├── preprocess_monuments()             # Create feature vectors
├── create_feature_vector()            # Combine features
├── apply_all_filters()                # Filter by preferences
│   ├── apply_category_filter()
│   ├── apply_budget_filter()
│   ├── apply_location_filter()
│   ├── apply_season_filter()
│   ├── apply_crowd_filter()
│   └── apply_weather_filter()
├── compute_similarity_scores()        # TF-IDF + Cosine Similarity
└── return recommendations             # Top 5 sorted by match score
```

### `monuments.csv` (Dataset)
```
monument_name,city,state,category,budget,best_season,crowd_level,weather_type,rating,description
Taj Mahal,Agra,Uttar Pradesh,UNESCO World Heritage,Moderate,October-March,High,Moderate,4.8,...
...25 total monuments
```

### `Frontend/templates/*.html`
- `index.html` - Home page with navigation
- `form.html` - Form for user preferences
- `results.html` - Display recommendations
- `about.html` - Project information

### `Frontend/static/style.css`
- Complete styling for all pages
- Responsive design
- Cards layout for recommendations

---

## 🔧 Configuration & Customization

### Add New Monuments

Edit `monuments.csv` and add a new row:
```csv
Monument Name,City,State,Category,Budget,Best Season,Crowd Level,Weather Type,Rating,Description
```

**Example:**
```csv
Meenakshi Temple,Madurai,Tamil Nadu,Temple,Low,January-March,High,Hot,4.5,"Historic Hindu temple..."
```

The system will automatically include it in recommendations on next run.

### Adjust Number of Recommendations

In `app.py`, change the `num_recommendations` parameter:

```python
# Current: returns 5 recommendations
recommendations = get_recommendations(user_prefs, num_recommendations=5)

# Change to 10 recommendations
recommendations = get_recommendations(user_prefs, num_recommendations=10)
```

### Change Flask Port

In `app.py`, modify the port number:

```python
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8000  # Change from 5000 to 8000
    )
```

Then access at: `http://127.0.0.1:8000/`

### Disable Debug Mode (Production)

```python
app.run(
    debug=False,  # Disable debug
    host='0.0.0.0',
    port=5000
)
```

---

## 🧪 Testing the System

### Test 1: Basic Recommendation
1. Go to `/form`
2. Select "Temple" category
3. Select "Moderate" budget
4. Click Submit
5. Should see temple recommendations

### Test 2: Location-Based
1. Go to `/form`
2. Select "Rajasthan" as state
3. Click Submit
4. Should see only Rajasthan monuments (Jaipur, Khimsar, etc.)

### Test 3: API Testing
Using Python/curl:
```bash
curl -X POST http://127.0.0.1:5000/api/get-recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "category": "Temple",
    "budget": "Moderate",
    "state_city": "Rajasthan",
    "season": "October",
    "crowd": "Moderate",
    "weather": "Moderate"
  }'
```

### Test 4: Terminal Output
When you submit a form, check the terminal for ML engine output:
```
================================================================================
Generating recommendations for user preferences:
  Category: Temple
  Budget: Moderate
  Location: Rajasthan
  Season: October
  Crowd: Moderate
  Weather: Moderate
================================================================================

📊 Loading monument database...
✓ Loaded 25 monuments from database

🔍 Applying filters...
✓ Filters applied: 5 monuments remain

⚙️ Vectorizing data...

📈 Computing similarity scores...
✓ Computed similarity scores for all monuments

✅ Generated 5 recommendations
```

---

## 📊 Sample Interaction Flow

### User Journey:
```
1. User visits http://127.0.0.1:5000/
   ↓
2. Clicks "Get Recommendation"
   ↓
3. Fills form:
   - Category: "Fort"
   - Budget: "Moderate"
   - Location: "Rajasthan"
   - Season: "October-March"
   ↓
4. Clicks "Submit"
   ↓
5. Form POST request to /results
   ↓
6. Flask collects form data
   ↓
7. Calls get_recommendations(user_prefs)
   ↓
8. ML Engine:
   - Loads 25 monuments
   - Filters to Rajasthan forts
   - Vectorizes with TF-IDF
   - Computes similarity scores
   - Returns top 5
   ↓
9. Flask renders results.html with recommendations
   ↓
10. User sees personalized monuments with match scores
```

---

## ⚠️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: monuments.csv not found"
**Solution:**
- Ensure `monuments.csv` is in the project root directory
- Check the file path: `C:\Users\sambh\OneDrive\Desktop\ML PROJECT\monuments.csv`

### Issue: "Address already in use: Port 5000"
**Solution:**
Either close the existing Flask server or use a different port:
```python
app.run(port=8000)  # Use port 8000 instead
```

### Issue: Frontend not showing styled
**Solution:**
- Verify `Frontend/static/style.css` exists
- Check that the Flask app is running with correct template folder path
- Verify HTML has correct CSS link: `<link rel="stylesheet" href="/Frontend/static/style.css" />`

### Issue: No recommendations returned
**Solution:**
- Make sure form fields aren't empty
- Check terminal for error messages
- Verify `monuments.csv` has data
- Try selecting different preferences

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **Machine Learning**
   - TF-IDF vectorization
   - Cosine similarity
   - Content-based filtering

2. **Web Development**
   - Flask backend
   - HTML/CSS frontend
   - Form handling

3. **Data Processing**
   - CSV data loading
   - Data preprocessing
   - Feature engineering

4. **Software Architecture**
   - Modular code structure
   - Separation of concerns
   - Clean code practices

---

## 📈 Enhancement Ideas

1. **Add Database**
   - Move CSV to SQLite/PostgreSQL
   - Store user preferences/history

2. **Collaborative Filtering**
   - Track which recommendations users click
   - Recommend based on similar users

3. **Advanced Features**
   - Real weather API integration
   - Google Maps integration for directions
   - User reviews and ratings system

4. **NLP Enhancement**
   - Parse user descriptions in natural language
   - Better understanding of preferences

5. **Deployment**
   - Deploy to Heroku, AWS, or Azure
   - Docker containerization
   - CI/CD pipeline

---

## 📞 Support & Documentation

### Key Files:
- `app.py` - Read comments for route details
- `recommendation.py` - Read function docstrings for ML logic
- `monuments.csv` - Check data structure

### Online Resources:
- Flask Documentation: https://flask.palletsprojects.com/
- Scikit-learn Docs: https://scikit-learn.org/
- Pandas Guide: https://pandas.pydata.org/

---

## ✅ Checklist Before Deployment

- [ ] Python 3.8+ installed
- [ ] `pip install -r requirements.txt` completed
- [ ] `monuments.csv` exists in root directory
- [ ] `Frontend/templates/` folder exists with HTML files
- [ ] `Frontend/static/` folder exists with CSS file
- [ ] Flask server starts without errors
- [ ] Web browser can access http://127.0.0.1:5000/
- [ ] Form submission works
- [ ] Recommendations display correctly

---

## 🎉 You're All Set!

Your Heritage AI recommendation system is complete and ready to use. Start the server and begin getting personalized monument recommendations!

```bash
python app.py
```

Then open: **http://127.0.0.1:5000/**

Enjoy exploring India's heritage! 🏛️
