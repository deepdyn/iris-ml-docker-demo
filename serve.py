# serve.py
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

app = FastAPI()
model = load("model.joblib")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(feat: IrisFeatures):
    X = np.array([[feat.sepal_length, feat.sepal_width,
                   feat.petal_length, feat.petal_width]])
    pred = int(model.predict(X)[0])
    return {"class": pred}

