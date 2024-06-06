import pytest
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from transport.models import Transport, Car, TypeTask, Status
from httpx import AsyncClient
from contextlib import nullcontext as does_not_raise


class TestTransort:

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "transport_create, status_code,  expectation, alert",
        [
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "status": Status.CREATED,
                    "destination": "test",
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-05-23 09:00:00",
                    "date_to": "2021-05-23 09:29:59",
                },
                201,
                does_not_raise(),
                "standart transport create",
            ),
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.CREATED,
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-05-23 08:30:00",
                    "date_to": "2021-05-23 09:29:59",
                },
                401,
                does_not_raise(),
                "unique transport created field data_to",
            ),
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.COMPLETED,
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-05-23 09:00:00",
                    "date_to": "2021-05-23 09:00:00",
                },
                401,
                does_not_raise(),
                "unique transport created data_from",
            ),
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.COMPLETED,
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-05-23 08:00:00",
                    "date_to": "2021-05-23 09:29:59",
                },
                401,
                does_not_raise(),
                "unique transport created data_from and date_to",
            ),
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.COMPLETED,
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-06-23 00:00:00",
                },
                201,
                does_not_raise(),
                "transport create without time",
            ),
            (
                {
                    "user_id": 1,
                    "notice": "Срочно",
                    "destination": "test",
                    "status": Status.COMPLETED,
                    "type_task": TypeTask.LOAD_UNLOAD,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2021-06-23 00:00:00",
                },
                201,
                does_not_raise(),
                "transport create without time not unique",
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
    @pytest.mark.parametrize(
        "transport_id, transport_update, status_code,  expectation, alert",
        [
            (
                4,
                {
                    "notice": "Срочно1",
                    "destination": "test1",
                    "type_task": "Подписать",
                    "status": Status.CREATED,
                    "contact": "+375297949210 Савосин Виталий",
                    "car_id": 1,
                    "date_from": "2025-06-23 00:00:00",
                },
                201,
                does_not_raise(),
                "standart transport update all filds",
            ),
            (
                4,
                {
                    "notice": "Срочно2",
                },
                201,
                does_not_raise(),
                "standart transport update one field",
            ),
            (
                4,
                {
                    "new_fild": "Срочно2",
                },
                201,
                does_not_raise(),
                "standart transport update non-existent field",
            ),
            (
                4,
                {
                    "date_from": "2020-05-24 10:30:00",
                    "date_to": "2020-05-24 11:30:00",
                },
                201,
                does_not_raise(),
                "Изменение дыты которая занята другой машиной, но свободна для текущей",
            ),
            (
                4,
                {
                    "car_id": 2,
                    "date_from": "2020-05-24 10:30:00",
                    "date_to": "2020-05-24 11:30:00",
                },
                401,
                does_not_raise(),
                "Изменение car_id и даты которая занята",
            ),
            (
                4,
                {
                    "car_id": 2,
                },
                401,
                does_not_raise(),
                "Изменение car_id и даты которая занята",
            ),
            (
                4,
                {
                    "date_from": "2025-05-24 10:30:00",
                    "date_to": "2025-05-24 11:30:00",
                },
                201,
                does_not_raise(),
                "unique update date_from or date_to filds",
            ),
            (
                3,
                {
                    "date_from": "2025-05-24 10:30:00",
                    "date_to": "2025-05-24 11:30:00",
                },
                401,
                does_not_raise(),
                "not unique update date_from and date_to filds",
            ),
            (
                4,
                {
                    "status": Status.CANCELED,
                    "date_from": "2025-05-24 12:30:00",
                },
                201,
                does_not_raise(),
                "update only date_from",
            ),
            (
                4,
                {
                    "date_to": "2021-06-23 13:30:00",
                },
                201,
                does_not_raise(),
                "update only date_to",
            ),
            (
                145,
                {
                    "date_to": "2021-06-23 13:30:00",
                },
                404,
                does_not_raise(),
                "error not found transport_id",
            ),
        ],
    )
    async def test_update_transport(
        self,
        ac: AsyncClient,
        transport_id: int,
        transport_update: dict,
        status_code: int,
        expectation,
        alert: str,
    ):
        with expectation:
            response = await ac.patch(
                f"/transport/{transport_id}", json=transport_update
            )
            assert response.status_code == status_code, alert

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "transport_id, status_code,  expectation, alert",
        [
            (
                3,
                204,
                does_not_raise(),
                "transport deleted",
            ),
            (
                7,
                404,
                does_not_raise(),
                "transport deleted not found id",
            ),
        ],
    )
    async def test_delete_transport(
        self,
        ac: AsyncClient,
        transport_id: int,
        status_code: int,
        expectation,
        alert: str,
    ):
        with expectation:
            response = await ac.delete(f"/transport/{transport_id}")
            assert response.status_code == status_code, alert
