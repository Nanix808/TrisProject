import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from users.models import User
from authorization.models import Role
from authorization.schemas import Role as RoleSchema


@pytest.fixture(scope="session")
def user_list():
    return [
        {
            "username": "User_1",
            "password_hash": "Password_1",
            "is_active": True,
            "role_id": 1,
        },
        {
            "username": "User_2",
            "password_hash": "Password_2",
            "is_active": True,
            "role_id": 1,
        },
        {
            "username": "User_3",
            "password_hash": "Password_3",
            "is_superuser": True,
            "role_id": 1,
        },
    ]


@pytest.fixture(scope="session")
def roles_list():
    return [
        {
            "name": "admin",
            "description": "Administrator",
            "permissions": {"a": "1", "b": 1},
        }
    ]


@pytest.fixture(scope="session", autouse=True)
async def test_create_roles_data_from_users(session: AsyncSession, roles_list):
    for role in roles_list:
        role = Role(**role)
        session.add(role)
    await session.commit()
    await session.refresh(role)


@pytest.fixture(scope="session", autouse=True)
async def test_create_users_data(session: AsyncSession, user_list):
    for user in user_list:
        user = User(**user)
        session.add(user)
    await session.commit()
    await session.refresh(user)
