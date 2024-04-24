from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

# from .models import Transport

# from authorization.crud import RolesCRUD

# from auth.utils import hash_password, create_refresh_jwt

# # from .exceptions import user_in_db_exc


# class TransportCRUD:
#     """Data Access Layer for operating user info"""

#     def __init__(self, db_session: AsyncSession):
#         self.db_session = db_session

#     async def get_users(self, *args, **kwargs) -> list[Transport]:
#         query = select(Transport)
#         result = await self.db_session.execute(query)
#         return result.scalars().all()
