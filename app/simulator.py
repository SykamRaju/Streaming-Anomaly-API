import pandas as pd
import time
import requests
import random

df = pd.read_csv("app/data/creditcard.csv").drop(columns=["Time", "Class"])

API_URL = "http://127.0.0.1:8000/predict"

print("Sending transactions to anomaly API...")

for i in range(10):  # simulate 10 transactions
    row = df.sample(1).iloc[0]
    payload = row.to_dict()
    response = requests.post(API_URL, json=payload)
    result = response.json()
    print(f"[{i+1}] Anomaly: {result['is_anomaly']} | Score: {result['anomaly_score']:.4f}")
    time.sleep(1)
