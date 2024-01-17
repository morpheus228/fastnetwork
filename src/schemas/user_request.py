from pydantic import BaseModel
from enum import Enum


class UserRequest(BaseModel):
    value: str


class UserRequestStatus(str, Enum):
    ACTIVE = 'active'
    AUTO_COMPLETED= 'autoCompleted'
    USER_COMPLETED= 'userCompleted'
    DELETED = 'deleted'

