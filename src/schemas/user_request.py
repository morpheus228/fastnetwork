from pydantic import BaseModel
from enum import Enum


class UserRequest(BaseModel):
    value: str