import streamlit as st
import pandas as pd
import requests
import random
import time

st.set_page_config(page_title="Streaming Anomaly Dashboard", layout="wide")
st.title("📈 Streaming Anomaly Detector (Live Demo)")

# Sample template to simulate new data
def generate_fake_transaction():
    return {
        "V1": random.uniform(-3, 3),
        "V2": random.uniform(-3, 3),
        "V3": random.uniform(-3, 3),
        "V4": random.uniform(-3, 3),
        "V5": random.uniform(-3, 3),
        "V6": random.uniform(-3, 3),
        "V7": random.uniform(-3, 3),
        "V8": random.uniform(-3, 3),
        "V9": random.uniform(-3, 3),
        "V10": random.uniform(-3, 3),
        "V11": random.uniform(-3, 3),
        "V12": random.uniform(-3, 3),
        "V13": random.uniform(-3, 3),
        "V14": random.uniform(-3, 3),
        "V15": random.uniform(-3, 3),
        "V16": random.uniform(-3, 3),
        "V17": random.uniform(-3, 3),
        "V18": random.uniform(-3, 3),
        "V19": random.uniform(-3, 3),
        "V20": random.uniform(-3, 3),
        "V21": random.uniform(-3, 3),
        "V22": random.uniform(-3, 3),
        "V23": random.uniform(-3, 3),
        "V24": random.uniform(-3, 3),
        "V25": random.uniform(-3, 3),
        "V26": random.uniform(-3, 3),
        "V27": random.uniform(-3, 3),
        "V28": random.uniform(-3, 3),
        "Amount": random.uniform(1, 1000),
    }

# Store recent predictions
if "predictions" not in st.session_state:
    st.session_state.predictions = []

backend_url = st.text_input("Backend API URL:", "https://streaming-anomaly-api.onrender.com/predict")

if st.button("Generate Transaction"):
    payload = generate_fake_transaction()
    try:
        response = requests.post(backend_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.session_state.predictions.insert(0, {
                "Amount": payload["Amount"],
                "Score": round(result["anomaly_score"], 4),
                "Anomaly": result["is_anomaly"]
            })
        else:
            st.error(f"Error from backend: {response.status_code}")
    except Exception as e:
        st.error(f"Request failed: {e}")

# Show recent predictions
if st.session_state.predictions:
    df = pd.DataFrame(st.session_state.predictions)
    st.subheader("📊 Recent Predictions")
    st.dataframe(df.style.applymap(lambda v: 'color:red' if v is True else '', subset=['Anomaly']))