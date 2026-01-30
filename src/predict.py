import joblib
import numpy as np
import os

MODEL_PATH = "models/random_forest.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

def load_artifacts():
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder

def predict_difficulty(features):
    """
    features: dict with keys
    ['enemy_density', 'health_pickups', 'accuracy_required', 'time_limit', 'map_complexity']
    """
    model, encoder = load_artifacts()

    import pandas as pd

    X = pd.DataFrame([features])


    pred_encoded = model.predict(X)[0]
    pred_label = encoder.inverse_transform([pred_encoded])[0]
    return pred_label

if __name__ == "__main__":
    sample_level = {
        "enemy_density": 80,
        "health_pickups": 2,
        "accuracy_required": 78,
        "time_limit": 110,
        "map_complexity": 8
    }

    prediction = predict_difficulty(sample_level)
    print(f"Predicted Difficulty: {prediction}")
