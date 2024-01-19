from pydantic import BaseModel
from enum import Enum


class UserCondition(str, Enum):
    NEW: str = "new"
    INTODUCTION_COMPLETED: str = "introductionCompleted"
    PROFILE_CREATED: str = "profileCreated"


class CreateUser(BaseModel):
    id: int
    first_name: str
    last_name: str|None
    username: str|None


class User(BaseModel):
    id: int
    first_name: str
    last_name: str|None
    username: str|None
    condition: UserCondition|None
    is_visible: bool|None


class UserUpdate(BaseModel):
    first_name: str|None
    last_name: str|None
    username: str|None
    condition: None|UserCondition