from fastapi import APIRouter


transport_router = APIRouter()


@transport_router.get("/")
async def get_timetable_for_day():
    return {"message": "Hello World"}
