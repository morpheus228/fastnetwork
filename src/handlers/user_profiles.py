from fastapi import Depends

from services import Service
from schemas import UserProfile


class UserProfilesHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def create(self, user_id: int, user_profile: UserProfile) -> str:
        pass
