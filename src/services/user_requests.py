from fastapi import HTTPException

from repositories import Repository
from schemas.user_request import UserRequest


class UserRequests:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository
        
    def create(self, user_id: int, user_request: UserRequest) -> int:
        user = self.repository.users.get_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        user_request_id = self.repository.user_requests.create(user_id, user_request)
        return user_request_id

        
    def get(self, user_id: int) -> list[UserRequest]:
        user = self.repository.users.get_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")
        
        user_requests = self.repository.user_requests.get(user_id)

        return [UserRequest(value=request.text) for request in user_requests]
    
    def get_by_id(self, request_id: int) -> UserRequest:
        user_request = self.repository.user_requests.get_by_id(request_id)

        if user_request is None:
            raise HTTPException(status_code=404, detail="The user request with the specified ID was not found")
        
        return UserRequest(value=user_request.text)



