from fastapi.testclient import TestClient
import pytest
from sqlalchemy import insert, select
from users.models import User
from users.schemas import UserCreate
from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

# from src.main import app
# from ..conftest import client


# async def test_create_users(session: AsyncSession):

#     stmt = insert(User).values(
#         [
#             {"username": "User_1", "password_hash": "Password_1"},
#             {"username": "User_2", "password_hash": "Password_2"},
#         ]
#     )
#     await session.execute(stmt)
#     await session.commit()
#     query = select(User)
#     result = await session.execute(query)
#     data = result.fetchall()
#     print(data)


# async def test_add_role2(session: AsyncSession):
# query = select(User).order_by(User.id)
# result = await session.execute(query)
# async with async_session_maker() as session:
# stmt = insert(User).values(
# username="admin",
# password_hash="Password",
# )
# await my_dependency.execute(stmt)
# await my_dependency.commit()
# query = select(User)
# result = await session.execute(query)
# data = result.scalars().all()
# print(data[1].username, data[1].password_hash, data[1].id)


# def test_auth():
#     response = client.get("/users/")
#     assert response.status_code == 200
#     assert 200 == 200


# async def test_auth2(ac: AsyncClient, user_list):
# response = await ac.get("/users/")
# assert response.status_code == 200
# assert len(response.json()) == 3
# assert response.json() == user_list
# print(response.json())


# def test_auth(test_create_users_data):
#     response = client.get("/users/")
#     print(response.json())
# assert response.status_code == 200
# assert 200 == 200
