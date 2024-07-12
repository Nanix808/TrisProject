from repository import AbstractRepository
from .models import User
from .schemas import UserCreate, UserUpdate
from .exceptions import user_in_db_exc
from auth.utils import hash_password, create_refresh_jwt

# from authorization.dependencies import role_service


class UserService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()

    async def add_user(self):
        pass

    async def get_users(self):
        users = await self.user_repo.find_all()
        return users

    async def user_by_id(self, id: int):
        users = await self.user_repo.get_by_id(id)
        return users

    async def get_by_filter(self, filter: dict):
        users = await self.user_repo.get_by_filter_user(filter)
        return users

    async def delete_is_active(self, id: int):
        users = await self.user_repo.delete_is_active(id)
        return users

    async def add_one(self, user_in: UserCreate):
        filter = {"username": user_in.username}
        user = await self.user_repo.get_by_filter(filter)
        if user:
            raise user_in_db_exc
        # check role
        if user_in.role_id is not None:
            user_in.role_id = None
            # role = await role_service.get_role_by_id(user_in.role_id)
            # if not role:
            #     user_in.role_id = None
        user_in.password_hash = hash_password(user_in.password_hash)
        user = User(**user_in.model_dump())
        user = await self.user_repo.add_one(user)
        return user

    async def update_user(
        self,
        user_id: int,
        user_update: UserUpdate,
    ):
        user = await self.user_repo.update(user_id, user_update)
        return user

    async def update_user_refresh_token(self, user: User, data: dict) -> User:
        refresh_tkn = create_refresh_jwt(payload=data)
        user_update = UserUpdate(**{"refresh_token": refresh_tkn})
        await self.update_user(user.id, user_update)
        return refresh_tkn
