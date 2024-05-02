import pytest
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from transport.models import Transport, Car, Status
from httpx import AsyncClient
from contextlib import nullcontext as does_not_raise


class TestTransort:

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
        "transport_create, status_code,  expectation, alert",
        [
            (
                {
                    "data": "17.05.2024",
                    "time": "16:00",
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.LOAD_UNLOAD.name,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2020-05-23 10:30:00",
                    "date_to": "2020-05-23 11:00:00",
                },
                201,
                does_not_raise(),
                "standart transport create",
            ),
            (
                {
                    "data": "17.05.2024",
                    "time": "16:00",
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.LOAD_UNLOAD.name,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2020-05-23 10:30:00",
                    "date_to": "2020-05-23 10:30:00",
                },
                401,
                does_not_raise(),
                "unique transport created",
            ),
        ],
    )
    async def test_create_transport(
        self,
        ac: AsyncClient,
        transport_create: dict,
        status_code: int,
        expectation,
        alert: str,
    ):
        with expectation:
            response = await ac.post("/transport/", json=transport_create)
            assert response.status_code == status_code, alert

    @pytest.mark.asyncio
    async def test_delete_all_transports(self, ac: AsyncClient):
        assert 1 == 1
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


# class Status(enum.Enum):
#     LOAD_UNLOAD = "загрузка/разгрузка"
#     PICKUP = "забрать"
#     SIGN = "подписать"


# class Transport(Base):
#     data: Mapped[str] = mapped_column(
#         String(30),
#         nullable=False,
#     )
#     time: Mapped[str | None] = mapped_column(String(30))
#     destination = mapped_column(String(150))
#     notice: Mapped[str | None] = mapped_column(String(500))
#     status: Mapped[Status] = mapped_column(nullable=True)
#     contact: Mapped[str | None] = mapped_column(String(50))
#     car: Mapped["Car"] = relationship("Car", back_populates="transport")


# class Car(TransportRelationMixin, Base):
#     _transport_back_populates = "car"

#     name: Mapped[str] = mapped_column(String(30))
