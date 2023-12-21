from repositories import Repository
from .users import Users


class Service:
	def __init__(self, repository: Repository):
		self.repository: Repository = repository

		self.users: Users = Users(self.repository)