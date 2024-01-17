from pydantic import BaseModel
from enum import Enum


class UserProfile(BaseModel):
    gender: str = None
    age: str = None
    soft_skills: str = None
    hard_skills: str = None
    hobbies: str = None