from jwt.exceptions import InvalidTokenError
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import (
    OAuth2PasswordBearer,
)


from src.auth.utils import utils as auth_utils

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login/",
)


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    return payload
