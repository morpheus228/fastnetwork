from sqlalchemy.orm import Session
from sqlalchemy import Engine

from schemas.user_profile import UserProfile
from .mysql import UserProfile as MysqlUserProfile


class UserProfilesMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
        
    def create(self, user_id: int, user_profile: UserProfile) -> int:
        with Session(self.mysql) as session:
            session.query(MysqlUserProfile).filter_by(user_id=user_id).update({'is_deleted': True})

            profile = MysqlUserProfile(user_id=user_id)
            session.add(profile)
            
            session.commit()
            return profile.id
        
    def get_by_id(self, profile_id: int) -> MysqlUserProfile|None:
        with Session(self.mysql) as session:
            return session.query(MysqlUserProfile).get(profile_id)
        
    def get(self, user_id: int) -> MysqlUserProfile|None:
        with Session(self.mysql) as session:
            return session.query(MysqlUserProfile).filter_by(user_id=user_id, is_deleted=False).first()
        
    def get_all(self, user_id: int) -> list[MysqlUserProfile|None]:
        with Session(self.mysql) as session:
            return session.query(MysqlUserProfile).filter_by(user_id=user_id).all()