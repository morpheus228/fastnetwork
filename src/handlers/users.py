from fastapi import Depends

from services import Service
# from handlers.middlewares import APIMiddleware
from schemas import User


class UsersHandler:
    def __init__(self, service: Service):
        self.service: Service = service
    
    # async def create(self, telegram_user: TelegramUser, bot_id: int = Depends(APIMiddleware.get_bot_id)) -> str:
    #     return await self.service.create(telegram_user, bot_id)

    async def create(self, user: User) -> str:
        pass
    
