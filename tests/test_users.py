from httpx import AsyncClient
from repositories import Repository
from schemas.user import CreateUser


users = [
    CreateUser(
        id=1425364,
        first_name="Anton",
        last_name="Sexsov",
        username="pidor"
        ),

    CreateUser(
        id=1364,
        first_name="Aton",
        last_name="Sexov",
        username="pidr"
        ),

    CreateUser(
        id=142,
        first_name="Anto",
        last_name="xsov",
        username="idr"
        ) 
]


async def test_error_creating_user(client: AsyncClient):
    response = await client.post('users/', json={})
    assert response.status_code == 422

    response = await client.post('users/', json={"id": 121212})
    assert response.status_code == 422


async def test_creating_user(client: AsyncClient, rep: Repository):
    response = await client.post('users/', json=users[0].dict())
    assert response.status_code == 200

    user = rep.users.get_by_id(users[0].id)
    assert user is not None
    assert user.id == users[0].id
    assert user.first_name == users[0].first_name
    assert user.last_name == users[0].last_name
    assert user.username == users[0].username


async def test_getting_user(client: AsyncClient, rep: Repository):
    response = await client.get(f'users/{users[0].id}')
    assert response.status_code == 200

    user = response.json()
    print(f"Userall: {type(user)}")
    assert user['id'] == users[0].id
    assert user['first_name'] == users[0].first_name
    assert user['last_name'] == users[0].last_name
    assert user['username'] == users[0].username
    assert user['condition'] == 'new'
    assert user['is_visible'] == True
    

async def test_already_creating_user(client: AsyncClient, rep: Repository):
    response = await client.post(f'users/', json=users[0].dict())
    assert response.status_code == 200


async def test_error_updating_user(client: AsyncClient, rep: Repository):
    response = await client.put(f'users/{users[0].id}', json={"condition": "a"})
    assert response.status_code == 422

    response = await client.put(f'users/{0}', json={"first_name": "Vasya"})
    assert response.status_code == 404


async def test_updating_user(client: AsyncClient, rep: Repository):
    response = await client.put(f'users/{users[0].id}', json={"condition": "introductionCompleted"})
    assert response.status_code == 200

    user = rep.users.get_by_id(users[0].id)
    assert user is not None
    assert user.condition == "introductionCompleted"
    assert user.first_name == users[0].first_name
    assert user.last_name == users[0].last_name
    assert user.username == users[0].username
