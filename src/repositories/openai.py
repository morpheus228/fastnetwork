import httpx

from config import Config
from .proxy import Proxy

from exceptions.local import *
from utils.time_logging import time_logging


class OpenAI:
    def __init__(self):
        self.proxy: Proxy = Proxy(
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {Config.openai.token}"
            }
        )

        self.embeddings_model = "text-embedding-ada-002"

    async def make_request(self, url: str, data: dict) -> dict:
        try:
            response = await self.proxy.post(url, data)
            return response.json()

        except httpx.ReadTimeout:
            raise OpenAIRequestTimeoutError
        
        except Exception as err:
            raise OpenAIRequestError(str(err))

    @time_logging
    async def get_embedding(self, text: str) -> list[float]:
        url = "https://api.openai.com/v1/embeddings"
        data = {"input": text, "model": self.embeddings_model}
        repsonse = await self.make_request(url, data)
        return repsonse['data'][0]['embedding']
