from pymongo import MongoClient
from pymongo.database import Database
from config import Config


def get_mongo() -> Database:
    config = Config.mongo
    client = MongoClient(host = config.host, port = int(config.port))
    return client[config.database]


PROFILE_EMBEDDINGS_COLLECTION = 'profile_embeddings'
REQUEST_EMBEDDINGS_COLLECTION = 'request_embeddings'
SUITABILITIES_COLLECTION = 'suitabilities'
