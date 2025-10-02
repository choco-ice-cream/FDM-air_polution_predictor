from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load the model
model = joblib.load("model/model.pkl")

app = FastAPI(title="Fast AI Server")


@app.post("/predict")
def predict(data: dict):
   
   
    
    prediction = 0
    return {"prediction": int(prediction)}