# import datetime
import bcrypt
import jwt
from jwt import ExpiredSignatureError
from config import settings
from datetime import timedelta, timezone, datetime


def create_access_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algoritm: str = settings.auth_jwt.algorithms,
    expire_timedelta: str | None = None,
    expire_minutes: int = settings.auth_jwt.accses_token_expire_minutes,
) -> str:
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, private_key, algorithm=algoritm)
    return encoded_jwt


def create_refresh_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algoritm: str = settings.auth_jwt.algorithms,
    expire_timedelta: str | None = None,
    expire_minutes: int = settings.auth_jwt.refresh_token_expire_minutes,
) -> str:
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, private_key, algorithm=algoritm)
    return encoded_jwt


def decode_jwt(
    token: str | bytes,
    publick_key: str = settings.auth_jwt.publick_key_path.read_text(),
    algoritm: str = settings.auth_jwt.algorithms,
) -> str:
    try:
        decoded_jwt = jwt.decode(token, publick_key, algorithms=algoritm)
    except ExpiredSignatureError:
        decoded_jwt = {}
    return decoded_jwt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode("utf-8")
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")


def validate_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
