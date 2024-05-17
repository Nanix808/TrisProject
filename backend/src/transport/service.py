from repository import AbstractRepository
from .shemas import TransportCreate, TransportUpdate
from .models import Transport
from .exceptions import (
    transport_in_db_exc,
    transport_not_found_exc,
    transport_in_db_time_exc,
)
import datetime


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
        # filter = {
        #     "data_from": transport_in.date_from,
        #     "data_to": transport_in.date_to,
        # }
        transport = await self.transport_repo.check_data(
            transport_in.date_from, transport_in.date_to
        )
        if transport:
            raise transport_in_db_time_exc
        transport = Transport(**transport_in.model_dump())
        transport = await self.transport_repo.add_one(transport)
        return transport

    async def delete_hard(self, transport_id: int):
        transport = await self.transport_repo.delete(transport_id)
        if not transport:
            raise transport_not_found_exc
        return transport

    async def update_transport(
        self, transport_id: int, transport_update: TransportCreate
    ):
        exclude_none = True
        start_datetime = transport_update.date_from
        end_datetime = transport_update.date_to
        if start_datetime or end_datetime:
            if end_datetime and not start_datetime:
                item = await self.transport_repo.get_by_id(transport_id)
                start_datetime = item.date_from
            elif start_datetime and not end_datetime:
                if start_datetime < datetime.datetime.now():
                    raise transport_in_db_time_exc
                end_datetime = None
                # item = await self.transport_repo.get_by_id(transport_id)
                # transport_update.notice = "item.notice"

                # transport_update = TransportUpdate(**dict(item.__dict__))
                # exclude_none = False
            elif start_datetime > end_datetime:
                raise transport_in_db_time_exc
            transport_items = await self.transport_repo.check_data(
                start_datetime, end_datetime
            )
            if transport_items:
                raise transport_in_db_time_exc
        transport = await self.transport_repo.update(
            transport_id, transport_update, exclude_none
        )
        if not transport:
            raise transport_not_found_exc
        return transport
