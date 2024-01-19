from fastapi.responses import JSONResponse
from services import Service
# from handlers.middlewares import APIMiddleware
from schemas import CreateUser, UserUpdate, User

from fastapi import Response


class UsersHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def get(self, user_id: int) -> User:
        user = self.service.users.get(user_id)
        return JSONResponse(content=user.dict())

    async def create(self, user: CreateUser) -> Response:
        self.service.users.create(user)
        return Response(status_code=200)
    
    async def update(self, user_id: int, user: UserUpdate) -> Response:
        self.service.users.update(user_id, user)
        return Response(status_code=200)

