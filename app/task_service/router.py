from fastapi import APIRouter


router = APIRouter(
    prefix="/task_service",
    tags=["Список задач"],
)