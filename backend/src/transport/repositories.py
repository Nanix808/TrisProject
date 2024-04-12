from .models import Transport
from repository import SQLAlchemyRepository


class TransportRepository(SQLAlchemyRepository):
    model = Transport
