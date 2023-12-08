import uvicorn
from fastapi import FastAPI, APIRouter

from repositories import Repository
from services import Service
from handlers import Handler


repository = Repository()
service = Service(repository)
handler = Handler(service)

app = FastAPI(title="Fastnetwork Main Backend")
handler.register(app)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=80)

