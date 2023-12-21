from fastapi import Depends

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

