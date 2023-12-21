from fastapi import Depends

from services import Service
from schemas import UserRequest


class UserRequestsHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def create(self, user_id: int, request: UserRequest) -> str:
        pass

    async def get(self, user_id: int) -> list[UserRequest]:
        pass

    async def get_by_id(self, id: int) -> UserRequest:
        pass