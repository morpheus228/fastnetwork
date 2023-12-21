from sqlalchemy import Engine
from pymongo.database import Database

from .mongo import get_mongo
from .mysql import get_mysql

from .openai import OpenAI

from .users_mysql import UsersMYSQL
from .profiles_mysql import UserProfilesMYSQL
from .recommendations_mysql import RecommendationsMYSQL

from .embeddings_mongo import EmbeddingsMongo
from .suitabilities_mongo import SuitabilitiesMongo


class Repository:
	def __init__(self):
		self.mysql: Engine = get_mysql()
		self.mongo: Database = get_mongo()

		self.openai: OpenAI = OpenAI()

		self.users: UsersMYSQL = UsersMYSQL(self.mysql)
		self.user_profiles: UserProfilesMYSQL = UserProfilesMYSQL(self.mysql)
		self.recommendations: RecommendationsMYSQL = RecommendationsMYSQL(self.mysql)

		self.embeddings: EmbeddingsMongo = EmbeddingsMongo(self.mongo)
		self.suitabilities: SuitabilitiesMongo = SuitabilitiesMongo(self.mongo)

