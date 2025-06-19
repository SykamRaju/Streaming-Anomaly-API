# Streaming-Anomaly-API

Streaming Anomaly API

# 🚨 Streaming-Anomaly-API

Real-time anomaly detection for credit card transactions using Isolation Forest and FastAPI.

## 🧠 Features

- Live anomaly detection via REST API
- Trained on credit card fraud dataset
- FastAPI backend
- Simulator script to test streaming

## ▶️ Run the app

```bash
# install dependencies
pip install -r requirements.txt

# run FastAPI server
uvicorn app.main:app --reload

# in another terminal, simulate transaction stream
python app/simulator.py
```
