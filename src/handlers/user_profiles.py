from fastapi import Response
from fastapi.responses import JSONResponse

from services import Service
from schemas import UserProfile


class UserProfilesHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def create(self, user_id: int, user_profile: UserProfile) -> JSONResponse:
        user_profile_id = self.service.user_profiles.create(user_id, user_profile)
        return JSONResponse(content={'user_profile_id': user_profile_id})
    
    async def get(self, user_id: int) -> UserProfile:
        return self.service.user_profiles.get(user_id)