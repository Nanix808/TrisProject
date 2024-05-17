from abc import ABC, abstractmethod

from sqlalchemy import select

from database import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    def get_by_id(id: id):
        """Retrieves entity by its identity"""
        raise NotImplementedError()


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, empty: dict) -> int:
        async with db_helper.session_dependency() as session:
            #     async def create_user(self, user_in: UserCreate, *args, **kwargs) -> User | None:
            # user = await self.get_user_by_username(user_in.username)
            # if user:
            #     raise user_in_db_exc
            # # check role
            # if user_in.role_id is not None:
            #     roles_crud = RolesCRUD(self.db_session)
            #     role = await roles_crud.get_role_by_id(user_in.role_id)
            #     if not role:
            #         # in not role in db reset role_id in None
            #         user_in.role_id = None
            # user_in.password_hash = hash_password(user_in.password_hash)
            # user = User(**user_in.model_dump())
            session.add(empty)
            await session.commit()
            await session.refresh(empty)
            return empty

    async def find_all(self):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def get_by_id(self, id: int, *args, **kwargs):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model).where(self.model.id == id)
            empty = await session.execute(stmt)
            empty = empty.scalars().first()
            if empty:
                return empty

    async def get_by_filter(self, filter):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model).filter_by(**filter)
            empty = await session.scalar(stmt)
            return empty

    async def update(self, id, data, exclude=True):
        async with db_helper.session_dependency() as session:
            empty = await session.get(self.model, id)
            for name, value in data.model_dump(exclude_unset=exclude).items():
                setattr(empty, name, value)
            await session.commit()
            return empty

    async def delete(self, id):
        async with db_helper.session_dependency() as session:
            empty = await session.get(self.model, id)
            if empty:
                await session.delete(empty)
                await session.commit()
            return empty
