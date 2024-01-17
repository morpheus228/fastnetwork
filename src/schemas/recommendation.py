from pydantic import BaseModel
from enum import Enum


class Recommendation(BaseModel):
    id: int
    profile_id: int


class RecommendationAnswerValue(str, Enum):
    LIKE: str = "like"
    SKIP: str = "skip"


class RecommendationAnswer(BaseModel):
    value: RecommendationAnswerValue