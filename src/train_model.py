import json
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load labeled data
with open("../data/labeled_incidents.json", "r") as f:
    incidents = json.load(f)

# Combine subject + body for model input
X = [i["subject"] + " " + i["body"] for i in incidents]
y = [i["label"] for i in incidents]

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = make_pipeline(
    TfidfVectorizer(),
    RandomForestClassifier(n_estimators=100, random_state=42)
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "../models/triage_model.pkl")
print("\n✅ Model saved to models/triage_model.pkl")
