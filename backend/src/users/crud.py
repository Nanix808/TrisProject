from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .models import User
from authorization.models import Role
from authorization.crud import RolesCRUD
from .schemas import UserCreate, UserUpdate, Role as RoleSchema
from auth.utils import hash_password, create_refresh_jwt
from .exceptions import user_in_db_exc


class UsersCRUD:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_users(self, *args, **kwargs) -> list[User]:
        query = select(User).options(joinedload(User.role)).order_by(User.id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_user(self, user_id: int, *args, **kwargs) -> User | None:
        query = (
            select(User)
            .where(User.id == user_id)
            .options(joinedload(User.role))
            .order_by(User.id)
        )
        user: User | None = await self.db_session.execute(query)
        user = user.scalars().first()
        if user:
            return user

    async def get_user_by_username(self, username: str, *args, **kwargs) -> User | None:
        query = select(User).where(User.username == username)
        user: User | None = await self.db_session.scalar(query)
        return user

    async def create_user(self, user_in: UserCreate, *args, **kwargs) -> User | None:
        user = await self.get_user_by_username(user_in.username)
        if user:
            raise user_in_db_exc
        # check role
        if user_in.role_id is not None:
            roles_crud = RolesCRUD(self.db_session)
            role = await roles_crud.get_role_by_id(user_in.role_id)
            if not role:
                # in not role in db reset role_id in None
                user_in.role_id = None
        user_in.password_hash = hash_password(user_in.password_hash)
        user = User(**user_in.model_dump())
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user

    async def update_user(
        self,
        user: User,
        user_update: UserUpdate,
        partial: bool = False,
    ) -> User:
        for name, value in user_update.model_dump(exclude_unset=partial).items():
            setattr(user, name, value)
        await self.db_session.commit()
        return user

    async def delete_user(self, user: User) -> None:
        setattr(user, "is_active", False)

        # await self.db_session.delete(user)
        await self.db_session.commit()

    async def update_user_refresh_token(self, user: User, data: dict) -> User:
        refresh_tkn = create_refresh_jwt(payload=data)
        setattr(user, "refresh_token", refresh_tkn)
        await self.db_session.commit()
        return refresh_tkn
