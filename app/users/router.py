from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Роутер для user"],
)