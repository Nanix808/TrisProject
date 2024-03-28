from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Role
from .schemas import Role as RoleSchema
from .exceptions import role_in_db_exc


class RolesCRUD:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_role_by_name(
        self, rolename: str, *args, **kwargs
    ) -> RoleSchema | None:
        query = select(Role).where(Role.name == rolename)
        role: Role | None = await self.db_session.scalar(query)
        return role

    async def get_role_by_id(self, id_role: int, *args, **kwargs) -> RoleSchema | None:
        query = select(Role)
        role: Role | None = await self.db_session.get(Role, id_role)
        return role

    async def get_roles(self, *args, **kwargs) -> list[RoleSchema]:
        query = select(Role).order_by(Role.id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    # async def get_user(self, user_id: int, *args, **kwargs) -> User | None:
    #     result = await self.db_session.get(User, user_id)
    #     return result

    # async def get_user_by_username(self, username: str, *args, **kwargs) -> User | None:
    #     query = select(User).where(User.username == username)
    #     user: User | None = await self.db_session.scalar(query)
    #     return user

    async def create_role(
        self, role_in: RoleSchema, *args, **kwargs
    ) -> RoleSchema | None:
        role = await self.get_role_by_name(role_in.name)
        if role:
            raise role_in_db_exc
        # check role
        # if user_in.role_id is not None:
        #     roles_crud = RolesCRUD(self.db_session)
        #     role = await roles_crud.get_role_by_id(user_in.role_id)
        #     if not role:
        # in not role in db reset role_id in None
        # user_in.role_id = None
        # user_in.password_hash = hash_password(user_in.password_hash)
        role = Role(**role_in.model_dump())
        self.db_session.add(role)
        await self.db_session.commit()
        await self.db_session.refresh(role)
        return role


#     async def update_user(
#         self,
#         user: User,
#         user_update: UserUpdate,
#         partial: bool = False,
#     ) -> User:
#         for name, value in user_update.model_dump(exclude_unset=partial).items():
#             setattr(user, name, value)
#         await self.db_session.commit()
#         return user

#     async def delete_user(self, user: User) -> None:
#         setattr(user, "is_active", False)

#         # await self.db_session.delete(user)
#         await self.db_session.commit()

#     async def update_user_refresh_token(self, user: User, data: dict) -> User:
#         refresh_tkn = create_refresh_jwt(payload=data)
#         setattr(user, "refresh_token", refresh_tkn)
#         await self.db_session.commit()
#         return refresh_tkn


# class RolesCRUD:
#     """Data Access Layer for operating user info"""

#     def __init__(self, db_session: AsyncSession):
#         self.db_session = db_session

#     async def get_role_by_id(self, id_role: int, *args, **kwargs) -> RoleSchema | None:
#         query = select(Role)
#         role: Role | None = await self.db_session.get(Role, id_role)
#         return role
