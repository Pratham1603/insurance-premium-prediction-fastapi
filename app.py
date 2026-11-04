from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from schema.user_input import UserInput
from config import tier_1_cities, tier_2_cities

# pip install fastapi uvicorn scikit-learn==1.5.1 pandas pydantic

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# model name from mlflow 
# dummy for now 
MODEL_VERSION = "1.0.0"

app = FastAPI()
        
# Human readable
@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

# Machine readable
@app.get('/health')
def health_check():
    return {"status": "healthy", "version": MODEL_VERSION, "model_loaded": model is not None}

# POST endpoint to predict insurance premium category based on user input
@app.post('/predict')
def predict_premium(data: UserInput):

    # since random forest model takes a dataframe as input, we will convert the pydantic model to a dataframe and then pass it to the model for prediction.
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})