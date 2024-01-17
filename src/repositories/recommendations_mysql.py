from sqlalchemy.orm import Session
from sqlalchemy import Engine

from .mysql import Recommendation


class RecommendationsMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
    
    def get(self, request_id: int) -> list[Recommendation]:
        with Session(self.mysql) as session:
            return session.query(Recommendation.profile_id)\
            .filter_by(request_id=request_id, is_selected=False)\
            .order_by(Recommendation.is_viewed, Recommendation.score.desc())\
            .limit(10)\
            .all()
        
    def update(self, recommendation_id: int, **kwargs):
        with Session(self.mysql) as session:
            session.query(Recommendation).filter_by(id=recommendation_id).update(kwargs)
            session.commit()

    def get_by_id(self, recommendation_id: int) -> Recommendation|None:
        with Session(self.mysql) as session:
            return session.query(Recommendation).get(recommendation_id)
        
        

            

