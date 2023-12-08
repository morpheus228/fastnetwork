from fastapi import APIRouter, FastAPI

# from .middlewares import APIMiddleware

from .users import UsersHandler

from services import Service


class Handler:
    def __init__(self, service: Service):
        # APIMiddleware.auth_service = service.auth

        self.users = UsersHandler(service)

    def register(self, app: FastAPI) -> list[APIRouter]:
        self.users_router = APIRouter(prefix="/users", tags=["Users"])
        self.users_router.add_api_route("/", endpoint=self.users.create, methods=["POST"])

        app.include_router(self.users_router)