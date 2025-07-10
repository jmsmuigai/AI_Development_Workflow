from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load your trained model (optional — only if you saved one using joblib)
# model = joblib.load("readmission_model.pkl")

app = Flask(__name__)

# Sample prediction function (mock logic for now)
def predict_readmission(data):
    # For demonstration, return True if patient age > 60 and diagnosis is diabetes
    age = data.get("age")
    diagnosis = data.get("diagnosis")
    if age and age > 60 and "diabetes" in diagnosis.lower():
        return True
    return False

@app.route('/')
def index():
    return "🏥 Welcome to the Hospital Readmission Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        result = predict_readmission(data)
        return jsonify({"readmission_risk": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
