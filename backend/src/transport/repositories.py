from datetime import datetime
from .models import Transport, Car
from repository import SQLAlchemyRepository
from database import db_helper
from sqlalchemy import select, or_, and_
from sqlalchemy.orm import joinedload


class TransportRepository(SQLAlchemyRepository):
    model = Transport

    async def check_data(
        self, start_datetime: datetime, end_datetime: datetime, car_id: int
    ):
        async with db_helper.session_dependency() as session:
            empty = None
            if end_datetime:
                stmt = (
                    select(self.model)
                    .options(
                        joinedload(self.model.user),
                    )
                    .filter(
                        and_(
                            self.model.car_id == car_id,
                            # self.model.date_to.isnot(None),
                            or_(
                                self.model.date_from.between(
                                    start_datetime, end_datetime
                                ),
                                self.model.date_to.between(
                                    start_datetime, end_datetime
                                ),
                                and_(
                                    self.model.date_from <= start_datetime,
                                    self.model.date_to >= end_datetime,
                                ),
                            ),
                        )
                    )
                )
                empty = await session.execute(stmt)
                empty = empty.scalars().all()
            return empty


class CarRepository(SQLAlchemyRepository):
    model = Car
