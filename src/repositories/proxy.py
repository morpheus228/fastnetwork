from fastapi import Response
import httpx

from config import Config


class Proxy:
    proxies = dict()

    def __init__(self, headers: dict = dict(), timeout: int = 10):
        self.headers: dict = headers
        self.timeout: int = timeout
        
    @classmethod
    def set(cls):
        cls.proxies = {
            'https://': Config.proxy.url,
            'http://': Config.proxy.url
        }

    async def post(self, url: str, data: dict = dict()) -> Response:
        async with httpx.AsyncClient(proxies=self.proxies) as client:
            return await client.post(url, headers=self.headers, json=data, timeout=self.timeout)
    
