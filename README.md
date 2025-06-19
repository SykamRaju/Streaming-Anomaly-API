# 🧠 Streaming Anomaly Detection API

Real-time anomaly detection for credit card transactions using Isolation Forest and FastAPI.

## 🚀 Project Summary

Real-time anomaly detection API using Isolation Forest on credit card transactions. Accepts live data and returns if it's an anomaly based on trained model.

![Python](https://img.shields.io/badge/Made%20With-Python-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![Deployed](https://img.shields.io/badge/Hosted%20On-Render%20+%20Streamlit-brightgreen)

- ✅ FastAPI backend
- ✅ Live simulation using Python script
- ✅ Deployed on Render (free tier)

## 🛰️ Live Demo

- 🔗 [FastAPI Backend (Swagger UI)](https://streaming-anomaly-api.onrender.com/docs)
- 📊 [Streamlit Dashboard (Frontend UI)](https://streaming-anomaly-api.streamlit.app)

## 🧠 Features

- Live anomaly detection via REST API
- Trained on credit card fraud dataset
- FastAPI backend
- Simulator script to test streaming

### 📥 Dataset (Not Included in Repo)

To use the full credit card dataset:

- Download it from: [Kaggle Credit Card Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Save it as: `app/data/creditcard.csv`

### Screenshots

![FastAPI Backend (Swagger UI)](https://raw.githubusercontent.com/SykamRaju/Streaming-Anomaly-API/refs/heads/main/app/static/screenshot1.png)

![Streamlit UI](https://raw.githubusercontent.com/SykamRaju/Streaming-Anomaly-API/refs/heads/main/app/static/screenshot2.png)

## ▶️ Run the app

```bash
# install dependencies
pip install -r requirements.txt

# run FastAPI server
uvicorn app.main:app --reload

# in another terminal, simulate transaction stream
python app/simulator.py
```
