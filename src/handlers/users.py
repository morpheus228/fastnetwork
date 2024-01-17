from services import Service
# from handlers.middlewares import APIMiddleware
from schemas import User, UserUpdate

from fastapi import Response


class UsersHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def create(self, user: User) -> Response:
        self.service.users.create(user)
        return Response(status_code=200)
    
    async def update(self, user_id: int, user: UserUpdate) -> Response:
        self.service.users.update(user_id, user)
        return Response(status_code=200)

