from repository import AbstractRepository
from .shemas import TransportCreate
from .models import Transport
from .exceptions import transport_in_db_exc

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
        filter = {"data": transport_in.data}
        transport = await self.transport_repo.get_by_filter(filter)
        if transport:
            raise transport_in_db_exc
        transport = Transport(**transport_in.model_dump())
        transport = await self.transport_repo.add_one(transport)
        return transport
