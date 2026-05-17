# 🏛️ Heritage AI - Historical Monument & Smart Tourism Recommendation System

<div align="center">

**An AI-Powered System to Discover India's Rich Cultural Heritage**

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](#)

</div>

---

## 🎯 Project Overview

**Heritage AI** is an intelligent tourism recommendation system that suggests historical monuments and heritage destinations based on user preferences using machine learning and content-based filtering.

### Key Features:
- 🤖 **ML-Powered Recommendations** - Uses TF-IDF vectorization and cosine similarity
- 📍 **Location-Based Filtering** - Filter by state and city
- 💰 **Budget-Aware** - Recommendations consider entrance fees and accessibility
- 🌤️ **Weather & Season Aware** - Suggests based on best visiting times
- 👥 **Crowd Preference** - Choose between quiet or busy destinations
- 🏆 **Rating System** - All monuments rated by tourists
- 💻 **Web-Based Interface** - Easy-to-use Flask web application
- 📱 **Responsive Design** - Works on desktop and mobile devices

---

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Project Structure](#-project-structure)
3. [How it Works](#-how-it-works)
4. [ML Algorithm Details](#-ml-algorithm-details)
5. [Installation](#-installation)
6. [Usage Guide](#-usage-guide)
7. [API Reference](#-api-reference)
8. [Dataset](#-dataset)
9. [Technology Stack](#-technology-stack)
10. [Future Enhancements](#-future-enhancements)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 5-Step Installation

```bash
# 1. Navigate to project directory
cd ML PROJECT

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify dataset exists
ls monuments.csv

# 4. Start Flask server
python app.py

# 5. Open browser
# Visit: http://127.0.0.1:5000/
```

**That's it!** 🎉

---

## 📁 Project Structure

```
ML PROJECT/
│
├── 📄 app.py                          ← Flask backend (CORE)
├── 📄 recommendation.py               ← ML engine (CORE)
├── 📄 monuments.csv                   ← Dataset (25 monuments)
├── 📄 requirements.txt                ← Dependencies
│
├── Frontend/
│   ├── templates/
│   │   ├── index.html               ← Home page
│   │   ├── form.html                ← Recommendation form
│   │   ├── results.html             ← Results display
│   │   └── about.html               ← Project info
│   └── static/
│       └── style.css                ← Complete styling
│
├── SETUP.md                          ← Detailed setup guide
└── README.md                         ← Project documentation (THIS FILE)
```

---

## 🤖 How It Works

### User Journey

```
┌─────────────────────────────────────────────────────────────┐
│ 1. User visits home page                                    │
│    ↓                                                        │
│ 2. Clicks "Get Recommendation"                              │
│    ↓                                                        │
│ 3. Fills preference form:                                   │
│    • Category (Temple, Fort, etc.)                          │
│    • Budget (Low, Moderate, High)                           │  
│    • Location (State/City)                                  │
│    • Season (Best time to visit)                            │
│    • Crowd level (Quiet vs Busy)                            │
│    • Weather preference                                     │
│    ↓                                                        │
│ 4. Form sent to Flask backend                               │
│    ↓                                                        │
│ 5. ML Engine Process:                                       │
│    a) Load 25 monuments from CSV                            │
│    b) Filter by user preferences                            │
│    c) Vectorize text using TF-IDF                           │
│    d) Calculate similarity scores                           │
│    e) Rank by match percentage                              │
│    ↓                                                        │
│ 6. Display Top 5 recommendations with:                      │
│    • Monument name & rating                                 │
│    • Location details                                       │
│    • Budget & best season                                   │
│    • Match score (0-100%)                                   │
└─────────────────────────────────────────────────────────────┘
```

### Example Output

```
📌 RECOMMENDED MONUMENTS

1. Amber Fort (4.7⭐)
   Location: Jaipur, Rajasthan
   Category: Fort
   Budget: Moderate | Season: October-March | Weather: Hot
   Crowd Level: High | Match Score: 95.2%
   Description: A majestic mountaintop fort palace with a blend of 
   Hindu and Mughal architecture. Offers spectacular views of Jaipur city.

2. Meenakshi Temple (4.5⭐)
   Location: Madurai, Tamil Nadu
   Category: Temple
   Budget: Low | Season: January-March | Weather: Hot
   Crowd Level: High | Match Score: 88.7%
   Description: A historic Hindu temple dedicated to Meenakshi...
   
... (3 more recommendations)
```

---

## 🧠 ML Algorithm Details

### Algorithm: Content-Based Filtering with TF-IDF & Cosine Similarity

#### Step 1: Feature Extraction
Each monument is represented by combining multiple features:

```python
Features = [
    monument_name,      # "Taj Mahal"
    category,          # "UNESCO World Heritage"
    city,              # "Agra"
    state,             # "Uttar Pradesh"
    budget,            # "Moderate"
    best_season,       # "October-March"
    crowd_level,       # "High"
    weather_type,      # "Moderate"
    description        # "An iconic white marble mausoleum..."
]
```

#### Step 2: TF-IDF Vectorization
Convert text features to numerical vectors:

```
TF-IDF = Term Frequency × Inverse Document Frequency

Example:
- Word "temple" appears in 5/25 monuments → lower IDF weight
- Word "mausoleum" appears in 1/25 monuments → higher IDF weight
```

**Why TF-IDF?**
- Weights words by importance
- Common words get low weight
- Specific/distinctive words get high weight

#### Step 3: User Preference Vector
Create a similar vector from user inputs:

```python
User_Vector = TF-IDF([category, budget, location, season, crowd, weather])
```

#### Step 4: Similarity Calculation
Calculate cosine similarity between user vector and monument vectors:

```
Cosine Similarity = (u · m) / (||u|| × ||m||)

Range: 0 to 1 (represented as 0-100%)
- 100% = Perfect match
- 50% = Moderate match  
- 0% = No match
```

#### Step 5: Filtering
Apply explicit filters:

```python
if user_selects_temple:
    FILTER monuments WHERE category CONTAINS "temple"

if user_selects_rajasthan:
    FILTER monuments WHERE state = "rajasthan" OR city = "rajasthan"

if user_selects_october:
    FILTER monuments WHERE best_season CONTAINS "october"

... apply all filters sequentially
```

#### Step 6: Ranking & Return
```python
filtered_monuments = apply_all_filters(monuments, user_prefs)
ranked = sorted(filtered_monuments, by=similarity_score, descending=True)
return top_5(ranked)
```

### Algorithm Complexity
- **Time Complexity:** O(n × m) where n=monuments, m=features
- **Space Complexity:** O(n × v) where v=vocabulary size
- **Average Runtime:** < 100ms for 25 monuments

### Why This Approach?

**Advantages:**
- ✅ Simple and transparent (easy to explain)
- ✅ Fast inference (real-time recommendations)
- ✅ No training required (ready to use immediately)
- ✅ Scalable (works with thousands of monuments)
- ✅ Easy to add new monuments (just add CSV row)

**When This Works Best:**
- Small to medium datasets (10-1000 items)
- Limited historical user data
- Need for interpretable recommendations
- Real-time inference requirements

---

## 📦 Installation

### System Requirements
- Python 3.8+
- 100MB disk space
- Internet connection (for pip)

### Detailed Installation

#### 1. Install Python
```bash
# Verify Python installation
python --version
# Should show: Python 3.8.x or higher
```

#### 2. Install Dependencies
```bash
# Navigate to project folder
cd "C:\Users\sambh\OneDrive\Desktop\ML PROJECT"

# Install all packages
pip install -r requirements.txt

# What gets installed:
# - Flask 2.3.3         (Web framework)
# - Pandas 2.0.3        (Data manipulation)
# - NumPy 1.24.3        (Numerical computing)
# - Scikit-learn 1.3.0  (Machine learning)
# - Werkzeug 2.3.7      (Flask utilities)
```

#### 3. Verify Installation
```bash
python -c "import flask, pandas, numpy, sklearn; print('✓ All packages installed')"
```

#### 4. Check Dataset
```bash
# Verify monuments.csv exists
ls monuments.csv

# Or on Windows
dir monuments.csv
```

---

## 💻 Usage Guide

### Starting the Application

```bash
# Navigate to project directory
cd "C:\Users\sambh\OneDrive\Desktop\ML PROJECT"

# Start Flask server
python app.py
```

### Expected Output
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

### Accessing the Web Application

1. **Home Page:** `http://127.0.0.1:5000/`
   - Project introduction
   - Navigation links

2. **Recommendation Form:** `http://127.0.0.1:5000/form`
   - Fill preference form
   - 7 input fields for customization

3. **Results:** `http://127.0.0.1:5000/results`
   - Auto-generated after form submission
   - Shows top 5 recommendations

4. **About:** `http://127.0.0.1:5000/about`
   - Project details
   - Technology explanation

### Using the Recommendation Form

**Available Options:**

| Field | Options | Example |
|-------|---------|---------|
| **Category** | Temple, Fort, UNESCO World Heritage, Monument, Palace, Buddhist Monument, Religious, Archaeological, Fort, Entertainment | Temple |
| **Budget** | Low, Moderate, High, Any | Moderate |
| **State/City** | Delhi, Rajasthan, Agra, Jaipur, Tamil Nadu, Karnataka, Any | Rajasthan |
| **Duration** | 1 day, 2-3 days, 4-7 days, 1+ weeks | 3 days |
| **Season** | Summer, Monsoon, Winter, Spring, October, March, January | October-March |
| **Crowd** | Low, Moderate, High, Any | Moderate |
| **Weather** | Hot, Moderate, Humid, Cold, Any | Moderate |

### Accessing the API

For programmatic access, use the JSON API:

```bash
curl -X POST http://127.0.0.1:5000/api/get-recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "category": "Temple",
    "budget": "Moderate",
    "state_city": "Rajasthan",
    "duration": "3 days",
    "season": "October",
    "crowd": "Moderate",
    "weather": "Moderate"
  }'
```

---

## 🔌 API Reference

### Endpoint: GET Recommendations

**URL:** `/api/get-recommendations`  
**Method:** `POST`  
**Content-Type:** `application/json`

#### Request Body
```json
{
  "category": "Temple",
  "budget": "Moderate",
  "state_city": "Rajasthan",
  "duration": "3 days",
  "season": "October",
  "crowd": "Moderate",
  "weather": "Moderate"
}
```

#### Response (Success)
```json
{
  "success": true,
  "count": 5,
  "message": "Successfully generated 5 recommendations",
  "recommendations": [
    {
      "monument": "Meenakshi Temple",
      "city": "Madurai",
      "state": "Tamil Nadu",
      "category": "Temple",
      "budget": "Low",
      "season": "January-March",
      "crowd_level": "High",
      "weather": "Hot",
      "rating": 4.5,
      "description": "A historic Hindu temple...",
      "match_score": 94.5
    },
    ...
  ]
}
```

#### Response (Error)
```json
{
  "success": false,
  "message": "Error: No data provided"
}
```

### Other Endpoints

**Health Check:**
```
GET /api/health
```

Response:
```json
{
  "status": "healthy",
  "message": "Heritage AI Backend is running"
}
```

---

## 📊 Dataset

### Dataset File: `monuments.csv`

**Columns:**
- `monument_name` - Name of the monument
- `city` - City location
- `state` - State/Province
- `category` - Historical category
- `budget` - Budget level (Low/Moderate/High)
- `best_season` - Best time to visit
- `crowd_level` - Expected crowd intensity
- `weather_type` - Weather conditions
- `rating` - Tourist rating (0-5)
- `description` - Monument description

**Sample Data:**
```csv
Taj Mahal,Agra,Uttar Pradesh,UNESCO World Heritage,Moderate,October-March,High,Moderate,4.8,An iconic white marble mausoleum...
Amber Fort,Jaipur,Rajasthan,Fort,Moderate,October-March,High,Hot,4.7,A majestic mountaintop fort palace...
```

**Total Monuments:** 25

**Monuments Included:**
1. Taj Mahal
2. India Gate
3. Hawa Mahal
4. Qutub Minar
5. Red Fort
6. Mysore Palace
7. Varanasi Ghats
8. Konark Sun Temple
9. Khajuraho Temples
10. Charminar
11. Kingdom of Dreams
12. Amber Fort
13. Jantar Mantar
14. Sanchi Stupa
15. Gateway of India
16. Fort Kochi
17. Meenakshi Temple
18. Hampi Ruins
19. Ajanta & Ellora Caves
20. Borobudur
21. Ranthambore Fort
22. Jaisalmer Fort
23. Victoria Memorial
24. Chitradurga Fort
25. Tirupati Temple

### Adding New Monuments

Edit `monuments.csv`:

```csv
YourMonumentName,City,State,Category,Budget,BestSeason,CrowdLevel,WeatherType,Rating,Description
```

Example:
```csv
Brihadeeshwara Temple,Thanjavur,Tamil Nadu,Temple,Low,January-March,Moderate,Hot,4.6,An 11th-century Hindu temple with remarkable architecture
```

---

## 🛠️ Technology Stack

### Backend
- **Framework:** Flask 2.3.3
- **Language:** Python 3.8+
- **Server:** Werkzeug (built into Flask)

### Machine Learning
- **Primary Library:** Scikit-learn 1.3.0
- **Algorithms:** TF-IDF Vectorizer, Cosine Similarity
- **Data Processing:** Pandas 2.0.3, NumPy 1.24.3

### Frontend
- **Markup:** HTML5
- **Styling:** CSS3
- **Responsiveness:** Mobile-friendly design

### Deployment
- **Local:** Flask development server
- **Optional:** Heroku, AWS, Azure, Docker

### Database
- **Local:** CSV (monuments.csv)
- **Alternative:** SQLite, PostgreSQL

---

## 📈 ML Integration Explanation

### For Non-Technical Audience

**Think of it like a personal tour guide:**

1. **You describe your preferences:**
   - "I like temples"
   - "I have moderate budget"
   - "I prefer cool weather"

2. **The system learns your description:**
   - Converts words to mathematical representations
   - Understands "temple" is more important than budget

3. **The system compares with monuments:**
   ```
   Your preference score for:
   - Temple X       → 95% match ✓ (Best choice!)
   - Fort Y         → 40% match
   - Palace Z       → 35% match
   ```

4. **It ranks and recommends:**
   - Shows you the highest-matching temples first
   - Ranked by relevance (closest to your preferences)

### Mathematical Behind-the-Scenes

```
1. Text to Numbers:
   "temple rajasthan moderate" → [0.5, 0.8, 0.3, ...]

2. Calculate Distance:
   How different is your preference from each monument?
   Measured as "cosine similarity" (0 to 1)

3. Rank by Closeness:
   Closest = Best match → Show first
   Furthest = Worst match → Show last
```

**No fancy deep learning needed!** 🎓

---

## 🔮 Future Enhancements

### Phase 2 Features
- [ ] User accounts and saved preferences
- [ ] Rating system for recommendations
- [ ] Real-time weather API integration
- [ ] Google Maps integration
- [ ] Image gallery for each monument

### Phase 3 Features
- [ ] Collaborative filtering (recommend based on similar users)
- [ ] Seasonal crowd predictions
- [ ] Hotel/restaurant recommendations nearby
- [ ] Travel itinerary generation
- [ ] Budget optimization suggestions

### Phase 4 - Advanced
- [ ] Natural language processing for descriptions
- [ ] Deep learning models for better recommendations
- [ ] Mobile app (iOS/Android)
- [ ] Multi-language support
- [ ] AR feature to visualize monuments

### Deployment Options
- [ ] Docker containerization
- [ ] Heroku deployment
- [ ] AWS Lambda + DynamoDB
- [ ] Azure App Service
- [ ] Google Cloud Run

---

## 🐛 Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Python not found | Not installed | Install Python 3.8+ |
| ModuleNotFoundError: flask | Dependencies not installed | Run `pip install -r requirements.txt` |
| Port 5000 already in use | Another app using it | Use different port: `app.run(port=8000)` |
| monuments.csv not found | File in wrong location | Place CSV in project root directory |
| No recommendations shown | Empty form submission | Fill at least one preference field |
| Styling not applied | CSS not loading | Verify `Frontend/static/style.css` exists |

---

## 📚 Learning Resources

### Understanding the ML
- [TF-IDF Vectorization](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting)
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Content-Based Filtering](https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering)

### Flask Development
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Python Data Science
- [Pandas Documentation](https://pandas.pydata.org/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/)
- [NumPy Tutorial](https://numpy.org/devdocs/user/)

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 👥 Contributing

Contributions are welcome! Feel free to:
- Add more monuments to the dataset
- Improve the ML algorithm
- Enhance the UI/UX
- Add new features

---

## 📞 Questions & Support

For detailed setup instructions, see: [SETUP.md](./SETUP.md)

### Quick Debug Guide
```bash
# Check Python version
python --version

# Test imports
python -c "import flask; import pandas; import sklearn; print('OK')"

# Run with verbose output
python -c "
from recommendation import get_recommendations
prefs = {'category': 'Temple', 'budget': 'Moderate'}
recs = get_recommendations(prefs)
print(f'Got {len(recs)} recommendations')
"
```

---

## 🎉 Thank You!

Thank you for exploring the Heritage AI recommendation system. We hope this project helps you discover India's incredible historical heritage!

**Happy exploring! 🏛️✨**

---

<div align="center">

**Made with ❤️ for heritage preservation and smart tourism**

*Last Updated: 2025*

</div>
