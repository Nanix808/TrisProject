import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from users.models import User
from httpx import AsyncClient
from contextlib import nullcontext as does_not_raise


class TestRole:

    # @pytest.mark.parametrize(
    #     "user_id, status_code",
    #     [(1, 200), (222, 404)],
    # )
    # @pytest.mark.asyncio
    # async def test_get_user_by_id(
    #     self,
    #     ac: AsyncClient,
    #     user_list: list,
    #     user_id: int,
    #     status_code: int,
    # ):

    #     response = await ac.get(f"/users/{user_id}")
    #     print(response.status_code)
    #     assert response.status_code == status_code, "users/ - not user returned"
    # if response.status_code == 200:
    #     user = response.json()
    #     assert user_list[0]["username"] == user["username"]

    # @pytest.mark.asyncio
    # async def test_get_users(self, ac: AsyncClient, user_list):
    #     response = await ac.get("/users/")
    #     assert response.status_code == 200, "users/ - not all users returned"
    #     assert len(response.json()) == len(user_list)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "role_create, status_code,  expectation, alert",
        [
            (
                {
                    "name": "test_user",
                    "description": "test_user",
                    "permissions": '{"a": "1", "b": 1}',
                },
                201,
                does_not_raise(),
                "standart user not create",
            ),
            (
                {
                    "name": "test_user",
                    "description": "test_unique",
                    "permissions": '{"a": "1", "b": 1}',
                },
                401,
                does_not_raise(),
                "unique user created",
            ),
            (
                {
                    "description": "test_unique",
                    "permissions": '{"a": "1", "b": 1}',
                },
                422,
                does_not_raise(),
                "no name role in requests",
            ),
            (
                {
                    "name": "test_user12",
                    "permissions": '{"a": "1", "b": 1}',
                },
                201,
                does_not_raise(),
                "without description role not created",
            ),
            (
                {
                    "name": "test_user",
                    "description": "test_unique",
                },
                422,
                does_not_raise(),
                "without permissions role not created",
            ),
        ],
    )
    async def test_create_role(
        self,
        ac: AsyncClient,
        role_create: dict,
        status_code: int,
        expectation,
        alert: str,
    ):
        with expectation:
            response = await ac.post("/authorization/", json=role_create)
            assert response.status_code == status_code, alert

    async def test_delete_all_role(self, ac: AsyncClient):
        pass
        # await session.execute(User.__table__.delete())
        # await session.commit()

        # response = await ac.post("/authorization/", json=role_create)
        # assert response.status_code == status_code

    # @pytest.mark.asyncio
    # async def test_delete_users(self, ac: AsyncClient, user_id: int = 2):
    #     response = await ac.delete(f"/users/{user_id}")
    #     assert response.status_code == 204
    #     response = await ac.get(f"/users/{user_id}")
    #     user = response.json()
    #     assert response.status_code == 200
    #     assert user["is_active"] == False
