from fastapi import Depends

from services import Service
from schemas import RecommendationAnswer


class RecommendationsHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def get(self, request_id: int) -> list[int]:
        pass

    async def answer(self, request_id: int, value: RecommendationAnswer):
        pass
