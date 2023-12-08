from fastapi import HTTPException, Request
import jwt

import services


# class APIMiddleware:
#     auth_service: services.Auth = None 

#     @classmethod
#     def get_bot_id(cls, request: Request):
#         api_key = request.headers['Authorization']

#         try:
#             return cls.auth_service.parse_jwt(api_key)
        
#         except Exception as err:
#             raise HTTPException(500, detail=err)