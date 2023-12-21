import asyncio
import uvicorn
from fastapi import FastAPI, APIRouter
from config import Config

from repositories import Repository
from repositories.proxy import Proxy
from services import Service
from handlers import Handler

import logging

logging.basicConfig(level=logging.INFO)


Config.set()
Proxy.set()

repository = Repository()
service = Service(repository)
handler = Handler(service)

app = FastAPI(title="Fastnetwork Main Backend")
handler.register(app)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=80)


def make_migrations():
    from repositories.mysql import Base
    Base.metadata.drop_all(repository.mysql)
    Base.metadata.create_all(repository.mysql)


async def main():
    # make_migrations()

    # user_id = 100
    # repository.users.create(user_id)

    # profile_id = repository.user_profiles.create(user_id)

    # embedding = [0.11, 0.22, 0.33, 0.44, 0.55]
    # repository.recommendations.create(profile_id, embedding)

    # repository.embeddings.create_profile(111, [0.55, 0.44, 0.33])
    # repository.embeddings.create_request(222, [0.55, 0.44, 0.33])

    # await Proxy().post("https://webhook-test.com/4009d81df2e80a9a80d4a1ac1f9461f7")
    # await repository.openai.get_embedding("Hello, World!")
    pass

# asyncio.run(main())