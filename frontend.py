import streamlit as st
import pickle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💰", layout="wide")

# Title
st.title("💰 Insurance Premium Category Predictor")
st.markdown("---")

# Load the ML model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("❌ Model file 'model.pkl' not found!")
        return None

model = load_model()
if model is None:
    st.stop()

# City tier definitions
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

all_cities = tier_1_cities + tier_2_cities

# Get trained occupations
try:
    cat_encoder = model.named_steps['preprocessor'].named_transformers_['cat']
    trained_occupations = sorted(list(cat_encoder.categories_[2]))
except:
    trained_occupations = ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']

# Input section
st.subheader("📝 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=119, value=30)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0, step=0.5)
    smoker = st.radio("Are you a smoker?", ["No", "Yes"])
    
with col2:
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0, step=0.5)

city = st.selectbox("City", all_cities, index=0)
occupation = st.selectbox("Occupation", trained_occupations)

st.markdown("---")

# Prediction button
if st.button("🔮 Predict Premium Category", type="primary", width='stretch'):
    try:
        # Convert smoker to boolean
        is_smoker = smoker == "Yes"
        
        # Calculate derived features
        bmi = weight / (height ** 2)
        
        # Age group
        if age < 25:
            age_group = "young"
        elif age < 45:
            age_group = "adult"
        elif age < 60:
            age_group = "middle_aged"
        else:
            age_group = "senior"
        
        # Lifestyle risk
        if is_smoker and bmi > 30:
            lifestyle_risk = "high"
        elif is_smoker or bmi > 27:
            lifestyle_risk = "medium"
        else:
            lifestyle_risk = "low"
        
        # City tier
        if city in tier_1_cities:
            city_tier = 1
        elif city in tier_2_cities:
            city_tier = 2
        else:
            city_tier = 3
        
        # Create input dataframe
        input_df = pd.DataFrame([{
            'bmi': bmi,
            'age_group': age_group,
            'lifestyle_risk': lifestyle_risk,
            'city_tier': city_tier,
            'income_lpa': income_lpa,
            'occupation': occupation
        }])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Prediction Results")
        
        col_result1, col_result2, col_result3 = st.columns(3)
        
        with col_result1:
            st.metric("Predicted Category", prediction)
        with col_result2:
            st.metric("BMI", f"{bmi:.1f}")
        with col_result3:
            st.metric("City Tier", city_tier)
        
        st.markdown("---")
        st.markdown("### 📈 Analysis Summary")
        
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
            st.write(f"**Age Group:** {age_group.title()}")
            st.write(f"**Lifestyle Risk:** {lifestyle_risk.title()}")
            st.write(f"**Smoker:** {'Yes' if is_smoker else 'No'}")
        
        with summary_col2:
            st.write(f"**Income:** ₹{income_lpa:.1f} LPA")
            st.write(f"**Height:** {height} m")
            st.write(f"**Weight:** {weight} kg")
        
        # Try to show probabilities
        try:
            probabilities = model.predict_proba(input_df)[0]
            classes = model.classes_
            
            st.markdown("---")
            st.markdown("### 🎯 Confidence Scores")
            
            prob_dict = {classes[i]: probabilities[i] for i in range(len(classes))}
            prob_df = pd.DataFrame(list(prob_dict.items()), columns=['Category', 'Confidence']).sort_values('Confidence', ascending=False)
            prob_df['Confidence %'] = (prob_df['Confidence'] * 100).round(2)
            
            st.bar_chart(prob_df.set_index('Category')['Confidence %'])
            st.dataframe(prob_df[['Category', 'Confidence %']], width='stretch', hide_index=True)
        except:
            pass
        
        st.success(f"✅ Based on your profile, you fall into the **{prediction}** premium category.")
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("Please check your input values and try again.")