from httpx import AsyncClient
from repositories import Repository
from schemas import CreateUser, UserRequest


user = CreateUser(
    id=988,
    first_name="Anton",
    last_name="Sexsov",
    username="pidor"
)

user_request = UserRequest(
    value = "Хочу секс"
)

# создаем пользователя
async def test_create_user(client: AsyncClient):
    response = await client.post(f'users/', json=user.dict())
    assert response.status_code == 200


async def test_get_recommendation(client: AsyncClient, rep: Repository):
    # создаем запрос, получаем его id
    response = await client.post(f'user_requests/{user.id}', json=user_request.dict())
    assert response.status_code == 200
    request_id = response.json()['user_request_id']

    # получаем рекомендации по запросу
    response = await client.get(f'recommendations/{request_id}')
    assert response.status_code == 200
    print(f"РЕКОМЕНДАЦИИ: {response.json()}")


