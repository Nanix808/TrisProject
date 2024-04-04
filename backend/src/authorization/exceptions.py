from fastapi import HTTPException, status


role_in_db_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="role is db",
    )


not_admin_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="user not admin",
)
