import pytest

from httpx import AsyncClient
from contextlib import nullcontext as does_not_raise


class TestRole:

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "role_create, status_code,  expectation, alert",
        [
            (
                {
                    "name": "test_role",
                    "description": "test_role",
                    "permissions": '{"a": "1", "b": 1}',
                },
                201,
                does_not_raise(),
                "standart role not create",
            ),
            (
                {
                    "name": "test_role",
                    "description": "test_role",
                    "permissions": '{"a": "1", "b": 1}',
                },
                401,
                does_not_raise(),
                "unique test_role created",
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
