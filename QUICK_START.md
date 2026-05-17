# 🚀 QUICK START - Heritage AI

## ⏱️ 5 Minute Setup

### Step 1: Install (1 minute)
```bash
pip install -r requirements.txt
```

### Step 2: Verify (30 seconds)
```bash
# Check CSV exists
ls monuments.csv
# or on Windows
dir monuments.csv
```

### Step 3: Run (30 seconds)
```bash
python app.py
```

### Step 4: Open (30 seconds)
```
http://127.0.0.1:5000/
```

### Step 5: Use (2 minutes)
- Click "Get Recommendation"
- Fill form
- Click "Submit"
- See recommendations!

---

## 📁 File Structure
```
app.py                    ← Flask backend
recommendation.py         ← ML engine
monuments.csv             ← Dataset (25 monuments)
requirements.txt          ← Dependencies
Frontend/templates/       ← HTML pages
Frontend/static/          ← CSS styling
```

---

## 🎯 What Each File Does

| File | Role |
|------|------|
| `app.py` | Handles web requests, serves pages |
| `recommendation.py` | ML recommendation engine (TF-IDF) |
| `monuments.csv` | Monument data with 10 features |
| `requirements.txt` | Python packages needed |

---

## 🔄 How It Works

```
User fills form
       ↓
app.py collects data
       ↓
recommendation.py processes (ML)
       ↓
Returns top 5 recommendations
       ↓
Results displayed on page
```

---

## 🤖 ML Algorithm

**Algorithm:** Content-Based Filtering with TF-IDF

```
1. Convert monument features to numbers (TF-IDF)
2. Convert user preferences to numbers
3. Calculate similarity (Cosine Similarity)
4. Filter by preferences
5. Rank by match score
6. Return top 5
```

**Time:** < 100ms per recommendation

---

## 🧪 Test It

### Basic Test
```bash
python app.py
# Then visit: http://127.0.0.1:5000/
```

### API Test
```bash
curl -X POST http://127.0.0.1:5000/api/get-recommendations \
  -H "Content-Type: application/json" \
  -d '{"category":"Temple","budget":"Moderate"}'
```

---

## ⚙️ Configuration

### Change Port
```python
# In app.py, last line:
app.run(port=8000)  # Change from 5000
```

### Add Monuments
```
Edit monuments.csv, add new row:
MyMonument,City,State,Category,Budget,Season,Crowd,Weather,Rating,Description
```

### Change Recommendations Count
```python
# In app.py:
recommendations = get_recommendations(user_prefs, num_recommendations=10)
```

---

## 🔌 API Endpoints

### Get Recommendations
```
POST /api/get-recommendations
Content-Type: application/json

{
  "category": "Temple",
  "budget": "Moderate",
  "state_city": "Rajasthan",
  "season": "October",
  "crowd": "Moderate",
  "weather": "Moderate"
}
```

### Health Check
```
GET /api/health
```

---

## 📊 Dataset Info

**25 Monuments included:**
- Taj Mahal, Amber Fort, Meenakshi Temple
- Qutub Minar, Red Fort, Gateway of India
- Hawa Mahal, Konark Sun Temple
- ...and 17 more!

**Features per monument:**
- Name, City, State
- Category, Budget, Season
- Crowd Level, Weather
- Rating, Description

---

## 📚 Documentation

- `README.md` - Full project docs
- `SETUP.md` - Detailed setup guide
- `INTEGRATION_GUIDE.md` - How ML connects to frontend

---

## ❓ Common Issues

**Problem:** "No module flask"
```bash
pip install -r requirements.txt
```

**Problem:** Port 5000 in use
```python
app.run(port=8000)  # Use different port
```

**Problem:** monuments.csv not found
```bash
# Verify file exists in project root
ls monuments.csv
```

**Problem:** No recommendations
- Fill at least one form field
- Check Flask is running

---

## 🎓 Key Concepts

### TF-IDF
- Converts text to numbers
- Weights important words higher
- Used to identify unique monument features

### Cosine Similarity
- Measures similarity between user and monument
- Score: 0 (no match) to 1 (perfect match)
- Shown as 0-100% on UI

### Content-Based Filtering
- Recommends similar items to user preferences
- No user history needed
- Works immediately with new users

---

## 📈 Performance

- **Recommendation time:** < 100ms
- **Database queries:** 0 (uses CSV)
- **Memory usage:** ~50-100 MB
- **Startup time:** < 2 seconds

---

## 🚀 Deployment Options

### Local (Current)
```bash
python app.py
```

### Production
```python
# In app.py, set debug=False
app.run(debug=False, host='0.0.0.0')
```

### Cloud (Optional)
- Heroku: Simple Flask deployment
- AWS Lambda: Serverless option
- Azure: Enterprise option
- Docker: Containerized option

---

## 📞 URLs

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:5000/ | Home page |
| http://127.0.0.1:5000/form | Get form |
| http://127.0.0.1:5000/results | Results page |
| http://127.0.0.1:5000/about | About page |
| http://127.0.0.1:5000/api/get-recommendations | API |

---

## ✨ What You Have

✅ Complete frontend (HTML/CSS)
✅ Flask backend (5 routes)
✅ ML recommendation engine
✅ 25 monument dataset
✅ Complete documentation
✅ API for external use
✅ Ready for project evaluation!

---

## 🎉 Start Now!

```bash
# Install
pip install -r requirements.txt

# Run
python app.py

# Visit
http://127.0.0.1:5000/

# Enjoy!
```

---

**For detailed info:** See README.md or SETUP.md
