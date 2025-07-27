# app/model.py

import joblib

# Load model once
model = joblib.load('model/fraud_model.pkl')

def predict(data_df):
    """Use the model to predict fraud."""
    result = model.predict(data_df)
    return int(result[0])  # 0 or 1
