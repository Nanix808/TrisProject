from typing import TYPE_CHECKING
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

import os

BASE_DIR = Path(__file__).parent.parent
DOTENV = os.path.join(os.path.join(BASE_DIR, ".env"))


class AuthJwt(BaseModel):
    publick_key_path: str = BASE_DIR / "certs" / "jwt-publick.pem"
    private_key_path: str = BASE_DIR / "certs" / "jwt-private.pem"
    algorithms: str = "RS256"
    tokenUrl: str = "/auth/login/"
    accses_token_expire_minutes: int = 1
    refresh_token_expire_minutes: int = 1


class Settings(BaseSettings):
    """Class Settings"""

    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8")

    auth_jwt: AuthJwt = AuthJwt()

    mode: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_echo: bool = True

    @property
    def DATABASE_URL_psycopg(self):
        """URL connect DB"""
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
