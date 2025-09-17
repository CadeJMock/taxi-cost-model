from pathlib import Path
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib            # <- pip install joblib

app = Flask(__name__)

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "model-files" / "nyc_taxi_meta_model.pkl"

def load_model(p):
    if not p.exists() or p.stat().st_size < 100:   # tiny file = suspicious
        raise RuntimeError(f"Model file missing or too small: {p}")
    try:
        return joblib.load(p)  # works for joblib-compressed or plain pickle
    except Exception as e:
        # Helpful hint if the file is text (e.g., wrong file or HTML)
        first = p.open("rb").read(32)
        raise RuntimeError(f"Failed to unpickle {p}. First bytes: {first!r}") from e

try:
    MODEL = load_model(MODEL_PATH)
except Exception as e:
    app.logger.error(e)
    MODEL = None

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/predict")
def predict():
    if MODEL is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    data = request.get_json(silent=True) or {}
    try:
        # ↓ Adjust these keys/order to match what your model expects
        feats = [
            int(data["passenger_count"]),
            float(data["trip_distance"]),
            int(data["pickup_hour"]),
            int(data["pickup_dow"]),
            float(data["pickup_lat"]),
            float(data["pickup_lng"]),
            float(data["dropoff_lat"]),
            float(data["dropoff_lng"]),
        ]
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": f"Bad input: {e}"}), 400

    X = np.array([feats])
    try:
        y = MODEL.predict(X)
        return jsonify({"prediction": float(y[0])})
    except Exception as e:
        return jsonify({"error": f"Inference error: {e}"}), 500

@app.get("/health")
def health():
    return {"ok": True, "model_loaded": MODEL is not None}
