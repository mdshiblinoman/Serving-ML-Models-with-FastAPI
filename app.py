from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Allowed occupations inferred from the trained encoder categories.
# This prevents runtime failures when an unseen category is passed.
try:
    _cat_encoder = model.named_steps['preprocessor'].named_transformers_['cat']
    _occupation_index = 2
    TRAINED_OCCUPATIONS = set(_cat_encoder.categories_[_occupation_index])
except Exception:
    TRAINED_OCCUPATIONS = set()

DEFAULT_OCCUPATION = sorted(TRAINED_OCCUPATIONS)[0] if TRAINED_OCCUPATIONS else None

app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

# human readable       
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict')
def predict_premium(data: UserInput):
    mapped_occupation = data.occupation
    note = None
    if TRAINED_OCCUPATIONS and data.occupation not in TRAINED_OCCUPATIONS and DEFAULT_OCCUPATION:
        mapped_occupation = DEFAULT_OCCUPATION
        note = (
            f"Occupation '{data.occupation}' is not present in the trained model. "
            f"Mapped to '{mapped_occupation}' for inference."
        )

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': mapped_occupation
    }])

    try:
        prediction = model.predict(input_df)[0]
    except ValueError as e:
        return JSONResponse(status_code=422, content={'detail': str(e)})

    response_payload = {'predicted_category': prediction}
    if note:
        response_payload['note'] = note
    return JSONResponse(status_code=200, content=response_payload)