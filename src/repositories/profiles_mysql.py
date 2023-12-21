from sqlalchemy.orm import Session
from sqlalchemy import Engine

from .mysql import UserProfile


class UserProfilesMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
        
    def create(self, user_id: int) -> int:
        with Session(self.mysql) as session:
            profile = UserProfile(user_id=user_id)
            session.add(profile)
            session.commit()
            return profile.id