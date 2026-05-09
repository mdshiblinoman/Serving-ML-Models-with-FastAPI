# 💰 Insurance Premium Category Predictor

A Streamlit-based web application that predicts insurance premium categories using machine learning.

## 🚀 Quick Start

```bash
# Navigate to project directory
cd "Serving ML Models with FastAPI"

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run frontend.py
```

Then open your browser to: **http://localhost:8502**

## 📚 Full Documentation

For complete step-by-step instructions, see [INSTRUCTIONS.md](INSTRUCTIONS.md)

## ✨ Features

- 🎯 Real-time premium category predictions
- 📊 Detailed analysis with confidence scores
- 🏙️ Support for 70+ Indian cities
- 💼 Multiple occupation categories
- 🔒 Local processing (no external API required)
- 🎨 User-friendly Streamlit interface

## 📋 What You Need

- Python 3.8+
- Dependencies listed in `requirements.txt`
- ML model file: `model.pkl`

## 🎮 How to Use

1. Enter your personal details (age, weight, height, income, etc.)
2. Select your smoking status, city, and occupation
3. Click **"Predict Premium Category"**
4. View your prediction and detailed analysis

## 📁 Project Files

| File | Purpose |
|------|---------|
| `frontend.py` | Main Streamlit application |
| `model.pkl` | Pre-trained ML model |
| `insurance.csv` | Training data sample |
| `ml_model.ipynb` | Model training notebook |
| `INSTRUCTIONS.md` | Detailed setup guide |

## 🔧 Troubleshooting

- **"model.pkl not found"** → Ensure you're in the correct directory
- **"ModuleNotFoundError"** → Run `pip install -r requirements.txt`
- **Port already in use** → Run with different port: `streamlit run frontend.py --server.port 8503`

For more help, see [INSTRUCTIONS.md](INSTRUCTIONS.md#-troubleshooting)

## 📊 Key Metrics

The model considers:
- **BMI** (calculated from weight/height)
- **Age Group** (young, adult, middle-aged, senior)
- **Lifestyle Risk** (based on smoking and BMI)
- **City Tier** (metro, tier-2, tier-3)
- **Income Level** (in LPA)
- **Occupation** (7 categories)

## 📝 Version

- **Python**: 3.8+
- **Streamlit**: 1.0+
- **Last Updated**: May 2026

---

**[View Complete Guide →](INSTRUCTIONS.md)**
