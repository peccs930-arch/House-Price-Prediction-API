from fastapi import FastAPI, HTTPException
from schema import HouseFeatures
from predict import load_model, predict_price

# Create FastAPI app
app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using a trained Machine Learning model.",
    version="1.0.0"
)

# Load model at startup
try:
    model = load_model("../model/house_price_model.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.get("/")
def home():
    return {
        "message": "Welcome to the House Price Prediction API!",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post("/predict")
def predict(features: HouseFeatures):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded."
        )

    try:
        prediction = predict_price(
            model=model,
            features=features
        )

        return {
            "prediction": {
                "predicted_house_price": round(prediction, 2),
                "currency": "USD"
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
