from .models import Role
from repository import SQLAlchemyRepository


class RoleRepository(SQLAlchemyRepository):
    model = Role
