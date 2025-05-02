import joblib

# Load trained model
model = joblib.load("../models/triage_model.pkl")

def classify_with_ml(incident):
    text = incident["subject"] + " " + incident["body"]
    prediction = model.predict([text])[0]
    return prediction
