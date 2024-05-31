from .models import Transport, Car
from repository import SQLAlchemyRepository
from database import db_helper
from sqlalchemy import select, or_


class TransportRepository(SQLAlchemyRepository):
    model = Transport

    async def check_data(self, start_datetime, end_datetime):
        async with db_helper.session_dependency() as session:
            empty = None
            if end_datetime:
                stmt = select(self.model).filter(
                    or_(
                        self.model.date_from.between(
                            start_datetime, end_datetime
                        ),
                        self.model.date_to.between(
                            start_datetime, end_datetime
                        ),
                    )
                )
                empty = await session.scalar(stmt)
            return empty


class CarRepository(SQLAlchemyRepository):
    model = Car
