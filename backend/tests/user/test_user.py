import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from users.models import User
from httpx import AsyncClient
from contextlib import nullcontext as does_not_raise


class TestUser:

    @pytest.mark.parametrize(
        "user_id, status_code",
        [(1, 200), (222, 404)],
    )
    @pytest.mark.asyncio
    async def test_get_user_by_id(
        self,
        ac: AsyncClient,
        user_list: list,
        user_id: int,
        status_code: int,
    ):

        response = await ac.get(f"/users/{user_id}")
        assert response.status_code == status_code, "users/ - not user returned"
        # if response.status_code == 200:
        #     user = response.json()
        #     assert user_list[0]["username"] == user["username"]

    @pytest.mark.asyncio
    async def test_get_users(self, ac: AsyncClient, user_list):
        response = await ac.get("/users/")
        assert response.status_code == 200, "users/ - not all users returned"
        assert len(response.json()) == len(user_list)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "user_create, status_code,  expectation",
        [
            (
                {
                    "username": "User_6",
                    "password_hash": "Password_66",
                    "role_id": 1,
                },
                201,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_2222",
                    "password_hash": "Password_66",
                },
                201,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_777",
                    "password_hash": "Password_22",
                    "role_id": "",
                },
                422,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_777",
                    "password_hash": "Password_22",
                    "role_id": "",
                },
                422,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_7",
                    "password_hash": "Password_22",
                    "role_id": 2,
                },
                201,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_6",
                    "password_hash": "Password_66",
                    "role_id": 1,
                },
                401,
                does_not_raise(),
            ),
            (
                {
                    "password_hash": "Password_66",
                    "role_id": 1,
                },
                422,
                does_not_raise(),
            ),
            (
                {
                    "username": "User_6",
                    "role_id": 1,
                },
                422,
                does_not_raise(),
            ),
        ],
    )
    async def test_create_users(
        self,
        ac: AsyncClient,
        user_create: dict,
        status_code: int,
        expectation,
    ):
        with expectation:
            response = await ac.post("/users/", json=user_create)
            assert response.status_code == status_code

    @pytest.mark.asyncio
    async def test_delete_users(self, ac: AsyncClient, user_id: int = 2):
        response = await ac.delete(f"/users/{user_id}")
        assert response.status_code == 204
        response = await ac.get(f"/users/{user_id}")
        user = response.json()
        assert response.status_code == 200
        assert user["is_active"] == False

    @pytest.mark.asyncio
    async def test_delete_users(self, ac: AsyncClient, user_id: int = 2):
        response = await ac.delete(f"/users/{user_id}")
        assert response.status_code == 204
        response = await ac.get(f"/users/{user_id}")
        user = response.json()
        assert response.status_code == 200
        assert user["is_active"] == False

    # @pytest.mark.asyncio
    # async def test_delete_all_user(self, ac: AsyncClient):
    #     await print(clean_db)
