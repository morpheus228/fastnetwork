from httpx import AsyncClient
from repositories import Repository
from schemas.user import CreateUser
from schemas.user_profile import UserProfile


user = CreateUser(
        id=23,
        first_name="Anton",
        last_name="Sexsov",
        username="pidor"
)

user_profile = UserProfile(
    gender = 'male',
    age = '10'
)

async def test_create_user(client: AsyncClient):
    response = await client.post(f'users/', json=user.dict())
    assert response.status_code == 200


async def test_error_creating_user_profile(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_profiles/{0}', json=user_profile.dict())
    assert response.status_code == 404


async def test_creating_user_profile(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_profiles/{user.id}', json=user_profile.dict())
    assert response.status_code == 200

    profile = rep.user_profiles.get_by_id(response.json()['user_profile_id'])
    assert profile is not None
    assert profile.user_id is user.id
    assert profile.is_deleted == False



async def test_already_creating_user_profile(client: AsyncClient, rep: Repository):
    response = await client.post(f'user_profiles/{user.id}', json=user_profile.dict())
    assert response.status_code == 200
    profile_id = response.json()['user_profile_id']

    profiles = rep.user_profiles.get_all(user.id)
    for profile in profiles:
        if profile.id == profile_id:
            assert profile.is_deleted == False
        else:
            assert profile.is_deleted == True


async def test_get_user_profile(client: AsyncClient):
    response = await client.post(f'user_profiles/{user.id}', json=user_profile.dict())
    assert response.status_code == 200
    profile_id = response.json()['user_profile_id']

    response = await client.get(f'user_profiles/{user.id}')
    assert response.status_code == 200
