from pydantic import BaseModel
from enum import Enum


class UserCondition(str, Enum):
    ACTIVE: str = "new"
    INTODUCTION_COMPLETED: str = "introductionCompleted"
    PROFILE_CREATED: str = "profileCreated"


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str


class UserUpdate(BaseModel):
    first_name: str|None
    last_name: str|None
    username: str|None
    condition: None|UserCondition