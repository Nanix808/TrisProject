from fastapi import HTTPException, status


transport_in_db_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="transport is db",
)


transport_not_found_exc = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="transport id not found",
)

transport_in_db_time_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="time is used",
)


car_in_db_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="car is db",
)

car_not_found_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="car id not found",
)
