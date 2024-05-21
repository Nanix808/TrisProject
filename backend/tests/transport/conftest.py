import datetime
import pytest

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient

from src.main import app
from transport.models import Transport, Car, TypeTask, Status
from auth.dependencies import get_current_active_auth_user


@pytest.fixture(scope="session")
def car_list():
    return [
        {
            "name": "reno",
        },
        {
            "name": "vw",
        },
    ]


@pytest.fixture(scope="session", autouse=True)
async def test_create_car_data(session: AsyncSession, car_list):
    for item in car_list:
        car = Car(**item)
        session.add(car)
    await session.commit()
    await session.refresh(car)


@pytest.fixture(scope="session")
def transport_list():

    Obj1 = datetime.datetime(
        year=2020,
        month=5,
        day=23,
        hour=10,
        minute=30,
    )
    return [
        {
            "user_id": 1,
            "status": Status.CREATED,
            "notice": "Срочно",
            "destination": "test",
            "type_task": TypeTask.LOAD_UNLOAD,
            "contact": "+375297949210 Савосин Виталий",
            "car_id": 1,
            "date_from": Obj1,
            "date_to": Obj1 + datetime.timedelta(hours=1),
        },
        {
            "user_id": 1,
            "status": Status.CREATED,
            "notice": "В течение часа",
            "destination": "test",
            "type_task": TypeTask.PICKUP,
            "contact": "+375297949210 Савосин Виталий",
            "car_id": 2,
            "date_from": Obj1 + datetime.timedelta(days=1),
            "date_to": Obj1 + datetime.timedelta(days=1, hours=1),
        },
    ]


@pytest.fixture(scope="session", autouse=True)
async def test_create_transport_data(session: AsyncSession, transport_list):
    for item in transport_list:
        trans = Transport(**item)
        session.add(trans)
    await session.commit()
    await session.refresh(trans)


# Initialise a test client
client = TestClient(app)


async def get_user():
    return (
        {
            "id": 1,
            "username": "User_1",
            # "password_hash": "Password_1",
            "is_active": True,
            "role_id": 1,
            "is_superuser": True,
        },
    )


app.dependency_overrides[get_current_active_auth_user] = get_user
