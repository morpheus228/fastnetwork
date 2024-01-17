from fastapi import Response

from services import Service
from schemas import RecommendationAnswer, Recommendation


class RecommendationsHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def get(self, request_id: int) -> list[Recommendation]:
        return self.service.recommendations.get(request_id)

    async def answer(self, recommendation_id: int, answer: RecommendationAnswer) -> Response:
        self.service.recommendations.answer(recommendation_id, answer.value)
        return Response(status_code=200)
