from sqlalchemy.orm import Session
from sqlalchemy import Engine

from schemas.user_request import UserRequest, UserRequestStatus
from .mysql import UserRequest as MysqlUserRequest


class UserRequestsMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql
        
    def create(self, user_id: int, user_request: UserRequest) -> int:
        with Session(self.mysql) as session:
            request = MysqlUserRequest(user_id=user_id, text=user_request.value)
            session.add(request)
            session.commit()
            return request.id
        
    def get_by_id(self, request_id: int) -> MysqlUserRequest|None:
        with Session(self.mysql) as session:
            return session.query(MysqlUserRequest).get(request_id)
        
    def get(self, user_id: int) -> list[MysqlUserRequest]:
        with Session(self.mysql) as session:
            return session.query(MysqlUserRequest).filter_by(user_id=user_id, status=UserRequestStatus.ACTIVE).order_by(MysqlUserRequest.created_at).all()