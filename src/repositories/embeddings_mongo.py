from pymongo.database import Database

from .mongo import *


class EmbeddingsMongo:
    def __init__(self, mongo: Database):
        self.mongo: Database = mongo
        
    def create_profile(self, profile_id: int, embedding: list[float]):
        self.mongo[PROFILE_EMBEDDINGS_COLLECTION].insert_one({
            'profile_id': profile_id,
            'embedding': embedding
        })
    
    def create_request(self, request_id: int, embedding: list[float]):
        self.mongo[REQUEST_EMBEDDINGS_COLLECTION].insert_one({
            'request_id': request_id,
            'embedding': embedding
        })

    def get_profile(self, profile_id: int) -> list[float]:
        return self.mongo[PROFILE_EMBEDDINGS_COLLECTION].find_one({"profile_id": profile_id})['embedding']
    
    def get_request(self, request_id: int) -> list[float]:
        return self.mongo[REQUEST_EMBEDDINGS_COLLECTION].find_one({"request_id": request_id})['embedding']