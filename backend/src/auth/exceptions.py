from fastapi import HTTPException, status


unauthed_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid username or password",
)


unactive_exc = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="user inactive",
)


token_invalide_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="token invalid",
)

token_invalide_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="acccess token invalid",
)


refresh_token_invalide_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="refresh token invalid (user not found)",
)
