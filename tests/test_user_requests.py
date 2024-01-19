from httpx import AsyncClient
from repositories import Repository
from schemas.user import CreateUser
from schemas.user_request import UserRequest, UserRequestStatus

user = CreateUser(
        id=54,
        first_name="Anton",
        last_name="Sexsov",
        username="pidor"
)

user_requests = [
    UserRequest(value="Хочу секс"),
    UserRequest(value="Хочу дружбу"),
    UserRequest(value="Хочу жену")
]


async def test_create_user(client: AsyncClient):
    response = await client.post(f'users/', json=user.dict())
    assert response.status_code == 200


# создаем запрос для несуществующего пользователя
async def test_error_creating_user_request(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_requests/{0}', json=user_requests[0].dict())
    assert response.status_code == 404


# создаем запрос, получаем из бд напрямую
async def test_creating_user_request(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_requests/{user.id}', json=user_requests[0].dict())
    assert response.status_code == 200

    request = rep.user_requests.get_by_id(response.json()['user_request_id'])
    assert request is not None
    assert request.user_id is user.id
    assert request.text == user_requests[0].value
    assert request.status == UserRequestStatus.ACTIVE


# создаем запрос, получаем c помощью заппроса по id
async def test_already_creating_user_profile(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_requests/{user.id}', json=user_requests[1].dict())
    assert response.status_code == 200
    request_id = response.json()['user_request_id']

    response = await client.get(f'user_requests/{request_id}')
    assert response.status_code == 200
    request = response.json()
    assert request['value'] == user_requests[1].value



async def test_get_user_requests(client: AsyncClient):
    response = await client.get(f'user_requests/list/{user.id}')
    assert response.status_code == 200

    requests = response.json()
    for i in range(len(requests)):
        assert requests[i]['value'] == user_requests[i].value