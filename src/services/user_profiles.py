from fastapi import HTTPException

from repositories import Repository
from schemas.user_profile import UserProfile


class UserProfiles:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository
        
    def create(self, user_id: int, user_profile: UserProfile) -> int:
        user = self.repository.users.get_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        user_profile_id = self.repository.user_profiles.create(user_id, user_profile)
        return user_profile_id

        
    def get(self, user_id: int) -> UserProfile|None:
        user = self.repository.users.get_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        user_profile = self.repository.user_profiles.get(user_id)

        if user_profile is None:
            raise HTTPException(status_code=404, detail="The user profile for user with the specified ID was not found")
        
        return UserProfile()



