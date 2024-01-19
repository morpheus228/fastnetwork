from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Engine

from repositories import Repository
from repositories.mysql import User
from schemas.user import UserUpdate, User


class Users:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository

    def get(self, user_id: int) -> User:
        mysql_user = self.repository.users.get_by_id(user_id)

        if mysql_user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        return User(
            id = mysql_user.id,
            first_name = mysql_user.first_name,
            last_name = mysql_user.last_name,
            username = mysql_user.username,
            is_visible = mysql_user.is_visible,
            condition = mysql_user.condition
        )
        
    def create(self, user: User) -> int:
        mysql_user = self.repository.users.get_by_id(user.id)

        if mysql_user is None:
            self.repository.users.create(user)

    def update(self, user_id: int, user: UserUpdate):
        mysql_user = self.repository.users.get_by_id(user_id)

        if mysql_user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        data = dict(filter(lambda item: item[1] is not None, user.dict().items()))
        self.repository.users.update(user_id, **data)
        

        