from repository import AbstractRepository


class TransportService:
    def __init__(self, transport_repo: AbstractRepository):
        self.transport_repo: AbstractRepository = transport_repo()

    async def add_user(self):
        pass

    async def get_transport(self):
        users = await self.transport_repo.find_all()
        return users
