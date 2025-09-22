from pydantic import BaseModel
from typing import List

class PredictionResponse(BaseModel):
    predictions: List[int]
    file: str
