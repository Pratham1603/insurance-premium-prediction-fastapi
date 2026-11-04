# Response model = used when sending response back to client at that time data is validated using this model.
# used at ending 

from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )