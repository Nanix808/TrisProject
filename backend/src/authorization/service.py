from repository import AbstractRepository
from .models import Role
from .schemas import BaseRole
from .exceptions import role_in_db_exc, role_not_in_db_exc


class RoleService:
    def __init__(self, role_repo: AbstractRepository):
        self.role_repo: AbstractRepository = role_repo()

    async def get_roles(self):
        roles = await self.role_repo.find_all()
        return roles

    async def create_role(self, role_in: BaseRole):
        filter = {"name": role_in.name}
        role = await self.role_repo.get_by_filter(filter)
        if role:
            raise role_in_db_exc
        role = Role(**role_in.model_dump())
        role = await self.role_repo.add_one(role)
        return role

    async def get_by_id(self, id: int):
        role = await self.role_repo.get_by_id(id)
        return role

    async def update_role(self, role_id: int, role_update: BaseRole):

        role = await self.role_repo.update(role_id, role_update, exclude=False)
        if not role:
            raise role_not_in_db_exc
        return role

    async def delete(self, role_id: int):
        role = await self.role_repo.delete(role_id)
        if not role:
            raise role_not_in_db_exc
        return role
