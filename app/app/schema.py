from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
    """
    Input schema for house price prediction.
    """

    area: float = Field(
        ...,
        gt=0,
        example=1500,
        description="Area of the house in square feet"
    )

    bedrooms: int = Field(
        ...,
        ge=1,
        le=10,
        example=3,
        description="Number of bedrooms"
    )

    bathrooms: int = Field(
        ...,
        ge=1,
        le=10,
        example=2,
        description="Number of bathrooms"
    )

    parking: int = Field(
        ...,
        ge=0,
        le=10,
        example=1,
        description="Number of parking spaces"
    )

    age: int = Field(
        default=5,
        ge=0,
        le=100,
        example=5,
        description="Age of the house (years)"
    )

    furnishing: int = Field(
        default=1,
        ge=0,
        le=2,
        example=1,
        description="0 = Unfurnished, 1 = Semi-Furnished, 2 = Furnished"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "area": 1500,
                "bedrooms": 3,
                "bathrooms": 2,
                "parking": 1,
                "age": 5,
                "furnishing": 1
            }
        }
