from typing import AsyncGenerator
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession


from src.main import app
from database import DatabaseHelper, db_helper
from config import settings
from models import Base
from users.models import User
from authorization.models import Role


db_helper_test = DatabaseHelper(settings.DATABASE_URL_psycopg, echo=False)

app.dependency_overrides[db_helper.get_scoped_session] = (
    db_helper_test.get_scoped_session
)
app.dependency_overrides[db_helper.session_dependency] = (
    db_helper_test.session_dependency
)
app.dependency_overrides[db_helper.scoped_session_dependency] = (
    db_helper_test.scoped_session_dependency
)


@pytest.fixture(scope="session", autouse=True)
async def init_tables():
    async with db_helper_test.engine.begin() as conn:
        assert settings.mode == "TEST", "mode must be TEST not found .test.env"
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
async def session():
    async with db_helper_test.session_factory() as session:
        yield session
        await session.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


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
