from typing import AsyncGenerator
import asyncio
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.main import app
from database import DatabaseHelper, db_helper
from config import settings
from models import Base
from users.models import User

import random

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


