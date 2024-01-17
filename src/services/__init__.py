from repositories import Repository

from .users import Users
from .user_profiles import UserProfiles
from .user_requests import UserRequests
from .recommendations import Recommendations


class Service:
	def __init__(self, repository: Repository):
		self.repository: Repository = repository

		self.users: Users = Users(self.repository)
		self.user_profiles: UserProfiles = UserProfiles(self.repository)
		self.user_requests: UserRequests = UserRequests(self.repository)
		self.recommendations: Recommendations = Recommendations(self.repository)