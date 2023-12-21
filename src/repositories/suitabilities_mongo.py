from pymongo.database import Database

from .mongo import *


class SuitabilitiesMongo:
    def __init__(self, mongo: Database):
        self.mongo: Database = mongo
        
    def create(self, profile_id: int, request_id: int, value: float):
        self.mongo[SUITABILITIES_COLLECTION].insert_one({
            'profile_id': profile_id,
            'request_id': request_id,
            'value': value
        })
    
    def get(self, profile_id: int, request_id: int) -> float:
        return self.mongo[SUITABILITIES_COLLECTION].find_one({
            'profile_id': profile_id,
            'request_id': request_id
        })

    def get_by_request_id(self, profile_id: int):
        return self.mongo[SUITABILITIES_COLLECTION].find({
            'profile_id': profile_id
        })

