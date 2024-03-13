# import pytest
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import insert, select
# from users.models import User


# @pytest.fixture(scope="session")
# def user_list():
#     return [
#         {
#             "username": "User_1",
#             "password_hash": "Password_1",
#             "email": None,
#             "phone": None,
#             "available": True,
#             "is_active": False,
#             "is_superuser": False,
            
#         },
#         {
#             "username": "User_2",
#             "password_hash": "Password_2",
#             "email": None,
#             "phone": None,
#             "available": True,
#             "is_active": False,
#             "is_superuser": False,
          
#         },
#         {
#             "username": "User_3",
#             "password_hash": "Password_3",
#             "email": None,
#             "phone": None,
#             "available": True,
#             "is_active": False,
#             "is_superuser": False,
         
#         },
#     ]


# @pytest.fixture(scope="session", autouse=True)
# async def test_create_users_data(session: AsyncSession, user_list):
#     # user_list = [
#     #     {"username": "User_1", "password_hash": "Password_1"},
#     #     {"username": "User_2", "password_hash": "Password_2"},
#     #     {"username": "User_3", "password_hash": "Password_3"},
#     # ]
#     for user in user_list:
#         user = User(**user)
#         session.add(user)
#     await session.commit()
#     await session.refresh(user)

#     # query = select(User)
#     # result = await session.execute(query)
#     # users = [x.serialize for x in result.scalars().all()]
#     # assert len(users) == 2, f"Expected 2 users, got {len(users)}"
#     # assert users == [{'id': 1, 'username': 'User_1'}, {'id': 3, 'username': 'User_2'}], f"Expected 2 users, got {users}"
