import pytest

import datetime

# import pytz
from sqlalchemy.ext.asyncio import AsyncSession
from transport.models import Transport, Car, Status


@pytest.fixture(scope="session")
def car_list():
    return [
        {
            "name": "reno",
            # "transport_id": 1,
        },
        {
            "name": "vw",
            # "transport_id": 2,
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
            "data": "18.05.2024",
            "time": "16:00",
            "notice": "Срочно",
            "destination": "test",
            "status": Status.LOAD_UNLOAD.name,
            "contact": "+375297949210 Савосин Виталий",
            "car_id": 1,
            "date_from": Obj1,
            "date_to": Obj1 + datetime.timedelta(hours=1),
        },
        {
            "data": "19.04.2024",
            "time": "13:00",
            "notice": "В течение часа",
            "destination": "test",
            "status": Status.PICKUP.name,
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


# yield
# await session.execute(User.__table__.delete())
# await session.execute(Role.__table__.delete())
# await session.commit()
