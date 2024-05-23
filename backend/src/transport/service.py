import datetime

from fastapi import Request
from repository import AbstractRepository

from .shemas import TransportCreate, TransportUpdate
from .models import Transport
from .exceptions import (
    transport_in_db_exc,
    transport_not_found_exc,
    transport_in_db_time_exc,
)

from authorization.exceptions import not_permission_exc


class TransportService:
    def __init__(self, transport_repo: AbstractRepository):
        self.transport_repo: AbstractRepository = transport_repo()

    async def get_by_filter(self, filter: dict):
        users = await self.transport_repo.get_by_filter(filter)
        return users

    async def get_transport(self):
        users = await self.transport_repo.find_all()
        return users

    async def add_transport(self, transport_in: TransportCreate):
        transport = await self.transport_repo.check_data(
            transport_in.date_from, transport_in.date_to
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

        if start_datetime or end_datetime:
            if end_datetime and not start_datetime:
                start_datetime = validate_transport.date_from
            elif start_datetime and not end_datetime:
                if start_datetime < datetime.datetime.now():
                    raise transport_in_db_time_exc
                transport_update["date_to"] = None
            elif start_datetime > end_datetime:
                raise transport_in_db_time_exc
            transport_items = await self.transport_repo.check_data(
                start_datetime, end_datetime
            )
            if transport_items and transport_items.id != transport_id:
                raise transport_in_db_time_exc

        update_data = validate_transport.model_copy(update=transport_update)

        transport = await self.transport_repo.update(
            transport_id, update_data, exclude=False
        )
        if not transport:
            raise transport_not_found_exc
        return transport
