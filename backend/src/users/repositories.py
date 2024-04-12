from .models import User
from repository import SQLAlchemyRepository
from database import db_helper
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class UserRepository(SQLAlchemyRepository):
    model = User

    async def find_all(self):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model).options(joinedload(User.role)).order_by(User.id)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def get_by_id(self, id: int, *args, **kwargs):
        async with db_helper.session_dependency() as session:
            stmt = (
                select(self.model)
                .where(self.model.id == id)
                .options(joinedload(User.role))
                .order_by(User.id)
            )
            user = await session.execute(stmt)
            user = user.scalars().first()
            if user:
                return user

    async def delete_is_active(self, id: int, *args, **kwargs):
        async with db_helper.session_dependency() as session:
            user = await session.get(self.model, id)
            setattr(user, "is_active", False)
            await session.commit()
