from fastapi import FastAPI
from app.schemas import IrisInput, PredictionOutput
import joblib
import numpy as np

# load model
model = joblib.load("model/iris_model.joblib")

# Iris class labels
class_labels = ['setosa', 'versicolor', 'virginica']

# create FastAPI app
app = FastAPI(title="Iris Flower Prediction API",
            description="An API to predict Iris flower species based on sepal and petal measurements.",
            version="1.0.0")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

@app.get("/info")
def model_info():
    """Model information endpoint"""
    return {
        "model_type": "RandomForestClassifier",
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "classes": class_labels
    }
    
@app.post("/predict", response_model=PredictionOutput)
def predict_species(data: IrisInput):
    """Predict the species of Iris flower"""
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    predicted_class = class_labels[prediction]
    return {"predicted_class": predicted_class}