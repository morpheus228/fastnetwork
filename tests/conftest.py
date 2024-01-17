import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
import pytest


from main import app, repository
from repositories import Repository
from repositories.mysql import Base


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


    
@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://127.0.0.1/") as client:
        yield client


@pytest.fixture(scope="session")
async def rep() -> Repository:
    yield repository


@pytest.fixture(autouse=True, scope="session")
async def prepare_mysql():
    Base.metadata.create_all(repository.mysql)
    yield
    Base.metadata.drop_all(repository.mysql)
