import datetime

from fastapi import Request
from repository import AbstractRepository

from .shemas import TransportCreate, TransportUpdate, CarUpdate
from .models import Transport, Car
from .exceptions import (
    transport_in_db_exc,
    transport_not_found_exc,
    transport_in_db_time_exc,
    car_in_db_exc,
    car_not_found_exc,
)

from authorization.exceptions import not_permission_exc


class TransportService:
    def __init__(self, transport_repo: AbstractRepository):
        self.transport_repo: AbstractRepository = transport_repo()

    async def get_by_filter(self, filter: dict):
        transport = await self.transport_repo.get_by_filter(filter)
        return transport

    async def get_transport(self):
        transport = await self.transport_repo.find_all()
        return transport

    async def get_transport_by_date(self, date, car_id):
        transport = await self.transport_repo.check_data(
            date, date.replace(minute=59, hour=23, second=59), car_id
        )
        return transport

    async def add_transport(self, transport_in: TransportCreate):
        transport = await self.transport_repo.check_data(
            transport_in.date_from, transport_in.date_to, transport_in.car_id
        )
        if transport:
            raise transport_in_db_time_exc
        transport = Transport(**transport_in.model_dump())
        transport = await self.transport_repo.add_one(transport)
        return transport

    async def delete_hard(self, transport_id: int, uid: int):
        transpotr_from_db = await self.transport_repo.get_by_id(transport_id)
        # Проверка может ли пользователь изменить транспорт
        # 0 если он суперадмин
        # или его id совпадает c transport.user_id
        if not transpotr_from_db:
            raise transport_not_found_exc
        if uid != transpotr_from_db.user_id and uid != 0:
            raise not_permission_exc
        transport = await self.transport_repo.delete(transport_id)
        if not transport:
            raise transport_not_found_exc
        return transport

    async def update_transport(
        self, transport_id: int, transport_update: TransportUpdate, uid: int
    ):
        transport_update = transport_update.model_dump(exclude_unset=True)
        transpotr_from_db = await self.transport_repo.get_by_id(transport_id)
        if not transpotr_from_db:
            raise transport_not_found_exc
        validate_transport = TransportUpdate.model_validate(
            transpotr_from_db, from_attributes=True
        )
        # Проверка может ли пользователь изменить транспорт
        # 0 если он суперадмин
        # или его id совпадает c transport.user_id
        if uid != transpotr_from_db.user_id and uid != 0:
            raise not_permission_exc

        start_datetime = transport_update.get("date_from", None)
        end_datetime = transport_update.get("date_to", None)
        car_id = transport_update.get("car_id", None)

        if start_datetime or end_datetime or car_id:
            if end_datetime and not start_datetime:
                start_datetime = validate_transport.date_from
            elif start_datetime and not end_datetime:
                # if start_datetime < datetime.datetime.now():
                #     raise transport_in_db_time_exc
                transport_update["date_to"] = None
            elif (
                start_datetime
                and end_datetime
                and start_datetime > end_datetime
            ):
                raise transport_in_db_time_exc
            elif car_id and not end_datetime and not start_datetime:
                start_datetime = validate_transport.date_from
                end_datetime = validate_transport.date_to
            transport_items = await self.transport_repo.check_data(
                start_datetime,
                end_datetime,
                transport_update.get("car_id", validate_transport.car_id),
            )
            if transport_items and transport_items[0].id != transport_id:
                raise transport_in_db_time_exc

        update_data = validate_transport.model_copy(update=transport_update)

        transport = await self.transport_repo.update(
            transport_id, update_data, exclude=False
        )
        if not transport:
            raise transport_not_found_exc
        return transport


class CarService:
    def __init__(self, car_repo: AbstractRepository):
        self.car_repo: AbstractRepository = car_repo()

    async def get_cars(self):
        cars = await self.car_repo.find_all()
        return cars

    async def add_cars(self, car_in):
        filter = {"name": car_in.name}
        car = await self.car_repo.get_by_filter(filter)
        if car:
            raise car_in_db_exc
        car = Car(**car_in.model_dump())
        car = await self.car_repo.add_one(car)
        return car

    async def update_cars(self, car_id: int, car_in):
        car = await self.car_repo.update(car_id, car_in, exclude=False)
        if not car:
            raise car_not_found_exc
        return car

    async def delete_cars(self, car_id: int):
        car = await self.car_repo.delete(car_id)
        if not car:
            raise car_not_found_exc
        return car
