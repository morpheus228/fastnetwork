from sqlalchemy.orm import Session
from sqlalchemy import Engine

from .mysql import ProfileEmbedding


class RecommendationsMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
        
    def create(self, profile_id: int, embedding: list[float]):
        with Session(self.mysql) as session:
            embedding = ProfileEmbedding(profile_id=profile_id, embedding=embedding)
            session.add(embedding)
            session.commit()