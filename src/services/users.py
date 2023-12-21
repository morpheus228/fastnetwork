from sqlalchemy.orm import Session
from sqlalchemy import Engine

from repositories import Repository
from repositories.mysql import User


class Users:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository
        
    def create(self, user: User) -> int:
        mysql_user = self.repository.users.get(user.id)

        if mysql_user is None:
            self.repository.users.create(user)