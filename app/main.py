from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.model import load_model, predict_anomaly

app = FastAPI(title="Streaming Anomaly Detection API")

model = load_model()

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.post("/predict")
def detect_anomaly(txn: Transaction):
    txn_df = pd.DataFrame([txn.dict()])
    prediction, score = predict_anomaly(model, txn_df.iloc[0])
    return {
        "is_anomaly": bool(prediction == -1),
        "anomaly_score": score
    }
