import joblib
import pandas as pd
from schema import HouseFeatures


def load_model(model_path: str):
    """
    Load the trained machine learning model.
    """
    model = joblib.load(model_path)
    return model


def prepare_input(features: HouseFeatures):
    """
    Convert the request data into a DataFrame
    matching the model's expected input format.
    """

    data = {
        "area": [features.area],
        "bedrooms": [features.bedrooms],
        "bathrooms": [features.bathrooms],
        "parking": [features.parking],
        "age": [features.age],
        "furnishing": [features.furnishing]
    }

    return pd.DataFrame(data)


def predict_price(model, features: HouseFeatures):
    """
    Predict the house price.
    """

    input_df = prepare_input(features)

    prediction = model.predict(input_df)

    return float(prediction[0])


if __name__ == "__main__":

    # Example usage (for testing)

    class DummyInput:
        area = 1500
        bedrooms = 3
        bathrooms = 2
        parking = 1
        age = 5
        furnishing = 1

    try:
        model = load_model("../model/house_price_model.pkl")

        price = predict_price(model, DummyInput())

        print(f"Predicted Price: ${price:,.2f}")

    except FileNotFoundError:
        print("Model file not found. Train your model and save it as:")
        print("../model/house_price_model.pkl")

    except Exception as e:
        print(f"Error: {e}")
