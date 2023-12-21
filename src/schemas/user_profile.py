from pydantic import BaseModel
from enum import Enum


class UserProfile(BaseModel):
    gender: str
    age: str 
    soft_skills: str = None
    hard_skills: str = None
    hobbies: str = None