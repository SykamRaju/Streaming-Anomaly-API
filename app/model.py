import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "anomaly_model.pkl")

def train_model():
    df = pd.read_csv("app/data/sample_creditcard.csv")
    features = df.drop(columns=["Time", "Class"])  # drop unnecessary columns
    clf = IsolationForest(contamination=0.001, random_state=42)
    clf.fit(features)
    joblib.dump(clf, MODEL_PATH)
    return clf

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        return train_model()

def predict_anomaly(model, data_row):
    score = model.decision_function([data_row])
    prediction = model.predict([data_row])
    return prediction[0], score[0]
