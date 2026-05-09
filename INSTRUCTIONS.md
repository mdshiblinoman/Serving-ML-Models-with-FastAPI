# Insurance Premium Category Predictor - Complete Setup Guide

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Installation Steps](#installation-steps)
5. [Running the Application](#running-the-application)
6. [How to Use the App](#how-to-use-the-app)
7. [Features](#features)
8. [Troubleshooting](#troubleshooting)
9. [File Descriptions](#file-descriptions)

---

## 🎯 Project Overview

This is an **Insurance Premium Category Predictor** web application built with **Streamlit**. It uses a pre-trained machine learning model to predict insurance premium categories based on user information.

**Key Features:**
- Simple, user-friendly interface
- Real-time predictions
- Detailed analysis with confidence scores
- No need for external API servers
- All processing done locally

---

## ✅ Prerequisites

Before you begin, ensure you have the following installed:

### System Requirements
- **Python 3.8 or higher** (3.9+ recommended)
- **pip** (Python package manager)
- **conda** (optional but recommended)
- **Git** (for version control)

### Check Your Python Version
```bash
python --version
```

If you need to install Python, download it from [python.org](https://www.python.org/downloads/)

---

## 📁 Project Structure

```
Serving ML Models with FastAPI/
│
├── frontend.py              # Main Streamlit application
├── app.py                   # Original FastAPI backend (reference)
├── model.pkl                # Pre-trained ML model
├── insurance.csv            # Training/sample data
├── ml_model.ipynb           # Jupyter notebook with model training
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── INSTRUCTIONS.md          # This file
```

---

## 🚀 Installation Steps

### Step 1: Clone or Navigate to Project Directory

```bash
cd "/home/noman/MyFiles/FastAPI/Serving ML Models with FastAPI"
```

### Step 2: Create a Python Virtual Environment (Optional but Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

**If `requirements.txt` doesn't exist, install manually:**
```bash
pip install streamlit pandas scikit-learn pickle5 numpy
```

### Step 4: Verify Model File

Ensure `model.pkl` exists in the project directory:
```bash
ls -la model.pkl   # On macOS/Linux
dir model.pkl      # On Windows
```

---

## ▶️ Running the Application

### Basic Command
```bash
streamlit run frontend.py
```

### Output
The app will start and display:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://192.168.0.107:8502
```

### Accessing the App

1. **Local Access**: Open your browser and go to `http://localhost:8502`
2. **Network Access**: On another computer on the same network, go to `http://192.168.0.107:8502`

### Stopping the App
Press `Ctrl + C` in the terminal where Streamlit is running.

---

## 🎮 How to Use the App

### Step-by-Step Guide

#### 1. **Enter Personal Information**
   - **Age**: Enter your current age (1-119 years)
   - **Weight**: Enter your weight in kilograms
   - **Height**: Enter your height in meters
   - **Annual Income (LPA)**: Enter annual income in Lakhs Per Annum
   - **Smoker Status**: Select "Yes" or "No"
   - **City**: Choose from available cities or enter a custom city
   - **Occupation**: Select your occupation from the dropdown

#### 2. **Review Input**
   - Double-check all values are correct
   - Ensure reasonable input values

#### 3. **Click "Predict Premium Category"**
   - Press the blue prediction button
   - Wait for the model to process

#### 4. **View Results**
   The app will display:
   - **Predicted Category**: Your insurance premium category
   - **BMI**: Calculated Body Mass Index
   - **City Tier**: Tier level of your city (1=Tier-1, 2=Tier-2, 3=Tier-3)
   - **Age Group**: Your age category
   - **Lifestyle Risk**: Risk assessment based on smoking and BMI
   - **Confidence Scores**: Probability distribution across categories

---

## ✨ Features

### Input Fields
- **Age Range**: 1-119 years
- **Weight Range**: 1.0 kg and above
- **Height Range**: 0.5-2.5 meters
- **Income Range**: 0.1 LPA and above
- **Cities**: 70+ Indian cities included
- **Occupations**: 7 categories (retired, freelancer, student, government_job, business_owner, unemployed, private_job)

### Calculated Features
The app automatically calculates:
- **BMI** (Body Mass Index) = Weight / (Height)²
- **Age Group**: young (<25), adult (25-44), middle_aged (45-59), senior (60+)
- **Lifestyle Risk**: high, medium, low (based on smoking status and BMI)
- **City Tier**: 1 (Metro), 2 (Tier-2), 3 (Tier-2/3)

### Output Predictions
The model predicts one of multiple insurance premium categories based on your profile.

---

## 🔧 Troubleshooting

### Issue 1: "model.pkl not found"
**Problem**: The app crashes with `FileNotFoundError: [Errno 2] No such file or directory: 'model.pkl'`

**Solution**:
- Ensure you're in the correct directory
- Verify `model.pkl` exists: `ls model.pkl`
- If missing, train the model using `ml_model.ipynb`

### Issue 2: "ModuleNotFoundError: No module named 'streamlit'"
**Problem**: Streamlit is not installed

**Solution**:
```bash
pip install streamlit
```

### Issue 3: "Port 8502 is already in use"
**Problem**: Another Streamlit app is running on the same port

**Solution**:
```bash
# Use a different port
streamlit run frontend.py --server.port 8503
```

### Issue 4: App runs but shows errors when predicting
**Problem**: Runtime errors during prediction

**Solution**:
- Check all input values are reasonable
- Ensure the model was trained correctly
- Check the browser console for error messages (F12)
- Try with default values first

### Issue 5: Connection refused error
**Problem**: Cannot access http://localhost:8502

**Solution**:
- Ensure Streamlit is still running
- Check the terminal for the correct port number
- Try http://127.0.0.1:8502 instead
- Clear browser cache (Ctrl+Shift+Delete)

---

## 📄 File Descriptions

### `frontend.py`
**Purpose**: Main Streamlit application
- Contains the entire web interface
- Loads the ML model
- Handles user input and predictions
- Displays results and analytics

### `app.py`
**Purpose**: Original FastAPI backend (reference only)
- Defines the data validation schema
- Lists all valid occupations and cities
- Implements the `/predict` endpoint
- No longer needed (integrated into Streamlit)

### `model.pkl`
**Purpose**: Pre-trained machine learning model
- Binary file containing the trained model
- Loaded by Streamlit app for predictions
- Created using scikit-learn's Pipeline

### `insurance.csv`
**Purpose**: Training/sample data
- Contains historical insurance data
- Used to train the ML model
- Can be used for testing/validation

### `ml_model.ipynb`
**Purpose**: Jupyter notebook with model development
- Data exploration and analysis
- Feature engineering
- Model training and evaluation
- Model saving to `model.pkl`

### `requirements.txt`
**Purpose**: Python dependencies list
- Lists all required packages
- Used by `pip install -r requirements.txt`
- Ensures reproducible environment

---

## 🎓 Understanding the Prediction

### What Factors Affect Your Premium Category?

1. **BMI (Body Mass Index)**
   - Calculated from height and weight
   - Higher BMI increases premium category
   - Threshold: 27 (medium), 30 (high)

2. **Age Group**
   - Younger individuals: lower premiums
   - Older individuals: higher premiums
   - Categories: young, adult, middle_aged, senior

3. **Smoking Status**
   - Smokers face higher premiums
   - Combined with BMI for lifestyle risk assessment

4. **Income Level**
   - Higher income may affect insurance tier
   - Measured in LPA (Lakhs Per Annum)

5. **City Tier**
   - Tier-1 cities (metros): higher costs
   - Tier-2 cities: moderate costs
   - Tier-3 cities: lower costs

6. **Occupation**
   - Different occupations have different risk profiles
   - Affects premium calculation

---

## 📊 Example Usage

### Scenario 1: Low-Risk Profile
```
Age: 25
Weight: 65 kg
Height: 1.75 m
Income: 8 LPA
Smoker: No
City: Bangalore
Occupation: private_job

Expected: Lower premium category
BMI: 21.2 (Healthy)
Lifestyle Risk: Low
```

### Scenario 2: High-Risk Profile
```
Age: 50
Weight: 90 kg
Height: 1.70 m
Income: 15 LPA
Smoker: Yes
City: Delhi
Occupation: business_owner

Expected: Higher premium category
BMI: 31.1 (Overweight)
Lifestyle Risk: High
```

---

## 🔒 Important Notes

- **Data Privacy**: No user data is stored or transmitted
- **Local Processing**: All computations happen on your computer
- **Model Accuracy**: Predictions depend on model quality and training data
- **Input Validation**: Invalid inputs will show error messages

---

## 📞 Support

If you encounter issues:

1. **Check this guide** for troubleshooting section
2. **Review error messages** in the terminal
3. **Check model file** exists: `ls model.pkl`
4. **Reinstall dependencies**: `pip install --upgrade streamlit pandas scikit-learn`
5. **Restart the app**: Stop with Ctrl+C and run again

---

## 🚀 Next Steps

After running the app successfully:

1. **Experiment** with different input values
2. **Observe** how changes affect predictions
3. **Explore** the confidence scores
4. **Review** the original notebook for model details
5. **Customize** the app as needed

---

## 📝 Version Information

- **Python**: 3.8+
- **Streamlit**: 1.0+
- **Pandas**: 1.0+
- **Scikit-learn**: 0.24+
- **Last Updated**: May 2026

---

## 📜 License

This project is for educational purposes.

---

**Happy Predicting! 🎉**
