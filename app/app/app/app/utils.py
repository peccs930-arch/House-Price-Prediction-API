import logging
import os
from datetime import datetime
import joblib


# -----------------------------
# Configure Logger
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("HousePriceAPI")


# -----------------------------
# Log Messages
# -----------------------------
def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)


# -----------------------------
# Check if Model Exists
# -----------------------------
def check_model(model_path: str):

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    return True


# -----------------------------
# Load Saved Model
# -----------------------------
def load_saved_model(model_path: str):

    check_model(model_path)

    model = joblib.load(model_path)

    log_info("Model loaded successfully.")

    return model


# -----------------------------
# Health Status
# -----------------------------
def health_status():

    return {
        "status": "running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# -----------------------------
# Prediction Response
# -----------------------------
def format_prediction(prediction):

    return {
        "success": True,
        "prediction": round(float(prediction), 2)
    }


# -----------------------------
# Error Response
# -----------------------------
def format_error(error):

    return {
        "success": False,
        "error": str(error)
    }


# -----------------------------
# Display API Information
# -----------------------------
def api_info():

    return {
        "project": "House Price Prediction API",
        "framework": "FastAPI",
        "version": "1.0.0",
        "author": "Your Name"
    }


# -----------------------------
# Test
# -----------------------------
if __name__ == "__main__":

    print(api_info())

    print(health_status())
