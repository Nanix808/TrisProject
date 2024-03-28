from fastapi import APIRouter, Depends, HTTPException, status

# from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import db_helper
from .schemas import (
    User,
    UserBase,
    UserCreate,
    UserUpdate,
    UserUpdatePartial,
)
from .crud import UsersCRUD
from .dependencies import user_by_id
from fastapi import HTTPException


user_router = APIRouter()


@user_router.get(
    "/",
    response_model=list[User],
)
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[User]:
    users_crud = UsersCRUD(session)
    users = await users_crud.get_users()
    return users


@user_router.post(
    "/",
    response_model=UserBase,
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:

    users_crud = UsersCRUD(session)
    users = await users_crud.create_user(user_in)
    return users


@user_router.get("/{user_id}", response_model=User)
async def get_user(user: User = Depends(user_by_id)):
    return user


@user_router.put("/{user_id}", response_model=UserUpdate)
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    users_crud = UsersCRUD(session)
    user = await users_crud.update_user(user=user, user_update=user_update)
    return user


@user_router.patch("/{user_id}")
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    users_crud = UsersCRUD(session)
    user = await users_crud.update_user(
        user=user, user_update=user_update, partial=True
    )
    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    users_crud = UsersCRUD(session)
    await users_crud.delete_user(user=user)


# @user_router.get("/auth", response_model=list[ShowResume])
# async def read_all_resume(db: AsyncSession = Depends(get_db)) -> list[ShowResume]:
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)
#             resume = await resume_dal.get_all_resume()
#     return resume


# @auth_router.get("/auth", response_model=list[ShowResume])
# async def read_all_resume(db: AsyncSession = Depends(get_db)) -> list[ShowResume]:
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)
#             resume = await resume_dal.get_all_resume()
#     return resume


# @get_data.get("/resume/{resume_id}", response_model=ShowResume)
# async def read_resume_by_id(resume_id, db : AsyncSession = Depends(get_db)) -> ShowResume:
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)
#             resume = await resume_dal.get_resume_by_id(
#                 resume_id=resume_id,

#             )
#             return resume


# @get_data.delete("/resume/del", response_model = Resume_Get_Id)
# async def delete_resume(resume_id: int,  db: AsyncSession = Depends(get_db)) -> Resume_Get_Id:
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)
#             resume = await resume_dal.delete_resume(resume_id=resume_id,)
#             if not resume:
#                 raise HTTPException(
#                 status_code=404, detail=f"Резюме с таким id {resume_id} не найдено."
#             )
#         return Resume_Get_Id(id=resume_id)


# @get_data.post("/resume/add", response_model=CreateShowResume)
# async def create_resume(body: ResumeCreate, db : AsyncSession = Depends(get_db)) -> CreateShowResume:
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)

#             resume_params = body.dict(exclude_none=True)
#             resume = await resume_dal.create_resume(
#                 resume_params
#             )
#             return resume


# @get_data.patch("/resume/update", response_model = Resume_Get_Id)
# async def update_resume_by_id(resume_id: int, body: UpdateResume, db: AsyncSession = Depends(get_db)) -> Resume_Get_Id:
#     updated_resume_params = body.dict(exclude_none=True)
#     if updated_resume_params == {}:
#         raise HTTPException(
#             status_code=422,
#             detail="Не предаставлены параметры для редактирования",
#         )
#     async with db as session:
#         async with session.begin():
#             resume_dal = ResumeDAL(session)
#             resume = await resume_dal.update_resume(
#                 resume_id=resume_id,
#                 updated_resume_params=updated_resume_params

#             )
#             if not resume:
#                 raise HTTPException(
#                 status_code=404, detail=f"Резюме с таким id {resume_id} не найдено."
#             )
#         return Resume_Get_Id(id=resume_id)
