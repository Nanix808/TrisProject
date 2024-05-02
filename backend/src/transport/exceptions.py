from fastapi import HTTPException, status


transport_in_db_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="transport is db",
    )

