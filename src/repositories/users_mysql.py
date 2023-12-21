from sqlalchemy.orm import Session
from sqlalchemy import Engine

from .mysql import User as MysqlUser
from schemas import User 


class UsersMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
        
    def create(self, user: User) -> int:
        with Session(self.mysql) as session:
            user = MysqlUser(id = user.id,
                             first_name = user.first_name,
                             last_name = user.last_name,
                             username = user.username)
            session.add(user)
            session.commit()

    def get(self, user_id: int) -> User|None:
        with Session(self.mysql) as session:
            user = session.query(MysqlUser).get(user_id)

            if user is None:
                return None
            
            return User(
                id = user.id,
                first_name= user.first_name,
                last_name = user.last_name,
                username = user.username
            )