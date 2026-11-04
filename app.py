from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from config.city_tier import tier_1_cities, tier_2_cities
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, MODEL_VERSION, model

# pip install fastapi uvicorn scikit-learn==1.5.1 pandas pydantic

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
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    # since random forest model takes a dataframe as input, we will convert the pydantic model to a dataframe and then pass it to the model for prediction.
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try :
            
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)}) 