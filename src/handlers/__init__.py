from fastapi import APIRouter, FastAPI

# from .middlewares import APIMiddleware

from .users import UsersHandler
from .user_profiles import UserProfilesHandler
from .user_requests import UserRequestsHandler
from .recommendations import RecommendationsHandler

from services import Service


class Handler:
    def __init__(self, service: Service):
        # APIMiddleware.auth_service = service.auth

        self.users = UsersHandler(service)
        self.user_profiles = UserProfilesHandler(service)
        self.user_requests = UserRequestsHandler(service)
        self.recommendations = RecommendationsHandler(service)
 
    def register(self, app: FastAPI) -> list[APIRouter]:
        self.users_router = APIRouter(prefix="/users", tags=["Users"])
        self.user_profiles_router = APIRouter(prefix="/user_profiles", tags=["UserProfiles"])
        self.user_requests_router = APIRouter(prefix="/user_requests", tags=["UserRequests"])
        self.recommendations_router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

        self.users_router.add_api_route("/{user_id}", endpoint=self.users.get, methods=["GET"])
        self.users_router.add_api_route("/", endpoint=self.users.create, methods=["POST"])
        self.users_router.add_api_route("/{user_id}", endpoint=self.users.update, methods=["PUT"])

        self.user_profiles_router.add_api_route("/{user_id}", endpoint=self.user_profiles.create, methods=["POST"])
        self.user_profiles_router.add_api_route("/{user_id}", endpoint=self.user_profiles.get, methods=["GET"])

        self.user_requests_router.add_api_route("/{user_id}", endpoint=self.user_requests.create, methods=["POST"])
        self.user_requests_router.add_api_route("/list/{user_id}", endpoint=self.user_requests.get, methods=["GET"])
        self.user_requests_router.add_api_route("/{id}", endpoint=self.user_requests.get_by_id, methods=["GET"])

        self.recommendations_router.add_api_route("/{request_id}", endpoint=self.recommendations.get, methods=["GET"])
        self.recommendations_router.add_api_route("/{request_id}", endpoint=self.recommendations.answer, methods=["POST"])

        app.include_router(self.users_router)
        app.include_router(self.user_profiles_router)
        app.include_router(self.user_requests_router)
        app.include_router(self.recommendations_router)