from enum import Enum


class RecommendationAnswer(str, Enum):
    like: str = "like"
    skip: str = "skip"