from fastapi import HTTPException

from repositories import Repository
from repositories.mysql import User
from schemas import Recommendation, RecommendationAnswerValue


class Recommendations:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository
        
    def get(self, request_id: int) -> list[Recommendation]:
        request = self.repository.user_requests.get_by_id(request_id)

        if request is None:
            raise HTTPException(status_code=404, detail="The user request with the specified ID was not found")
        
        recommendations = self.repository.recommendations.get(request_id)
        return [Recommendation(id=rec.id, profile_id=rec.profile_id) for rec in recommendations]
    
    def answer(self, recommendation_id: int, value: RecommendationAnswerValue) -> None:
        recommendation = self.repository.recommendations.get_by_id(recommendation_id)

        if recommendation is None:
            raise HTTPException(status_code=404, detail="The recommendation with the specified ID was not found")
        
        self.repository.recommendations.update(recommendation_id, is_viewed=True)

        if value == RecommendationAnswerValue.LIKE:
            self.repository.recommendations.update(recommendation_id, is_selected=True)


        



