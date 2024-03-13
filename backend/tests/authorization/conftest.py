import pytest

from sqlalchemy.ext.asyncio import AsyncSession
from authorization.models import Role
from users.models import User

@pytest.fixture(scope="session")
def roles_list_authorization():
    return [
        {
            "name": "admin1",
            "description": "Administrator",
            "permissions": {"a": "1", "b": 1},
        },
        {
            "name": "user2",
            "description": "user",
            "permissions": {"a": "1", "b": 1},
        },
    ]


@pytest.fixture(scope="session", autouse=True)
async def test_create_roles_data_from_role(
    session: AsyncSession, roles_list_authorization
):
    for role in roles_list_authorization:
        role = Role(**role)
        session.add(role)
    await session.commit()
    await session.refresh(role)
    # yield
    # await session.execute(User.__table__.delete())
    # await session.execute(Role.__table__.delete())
    # await session.commit()
