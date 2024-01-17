from fastapi import Depends
from fastapi.responses import JSONResponse

from services import Service
from schemas import UserRequest


class UserRequestsHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def create(self, user_id: int, user_request: UserRequest) -> JSONResponse:
        user_request_id = self.service.user_requests.create(user_id, user_request)
        return JSONResponse(content={'user_request_id': user_request_id})
    
    async def get(self, user_id: int) -> list[UserRequest]:
        return self.service.user_requests.get(user_id)

    async def get_by_id(self, id: int) -> UserRequest:
        return self.service.user_requests.get_by_id(id)