from fastapi import FastAPI
from app.users.schemas import User_Pydantic, UserIn_Pydantic
from app.division.schemas import Division_Pydantic, DivisionIn_Pydantic
from app.users.models import User
from app.division.models import Division
from app.database import init_db
from typing import List
from app.division.router import router as router_division
from app.users.router import router as router_users

app = FastAPI()
init_db(app)


@router_users.get("/", response_model=List[User_Pydantic])
async def get_users():
    """Тестовый вариант показ юзеров"""
    return await User_Pydantic.from_queryset(User.all())


@router_users.get("/{user_id}")
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router_division.post("/create",  response_model=Division_Pydantic)
async def division_add(division: DivisionIn_Pydantic):
    """Добавление Отдела"""
    division_obj = await Division.create(**division.model_dump(exclude_unset=True))
    return await Division_Pydantic.from_tortoise_orm(division_obj)


@router_division.get("/{division_id}")
async def division_get(division_id: int):
    """Поиск отдела по id"""
    return await Division_Pydantic.from_queryset_single(Division.get(id=division_id))


@router_division.get("/")
async def division_get():
    """Все отделы"""
    return await Division_Pydantic.from_queryset(Division.all())


@router_users.post("/create", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    """Тестовый вариант добавление юзера"""
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router_users.put("/{user_id}", response_model=User_Pydantic)
async def update_user(user_id: int, user: UserIn_Pydantic):
    """Тестовый вариант поиска юзера по id"""
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


app.include_router(router_division)
app.include_router(router_users)