from fastapi import FastAPI
from app.users.schemas import User_Pydantic, UserIn_Pydantic
from app.division.schemas import Division_Pydantic, DivisionIn_Pydantic
from app.users.models import User
from app.division.models import Division
from app.database import init_db
from typing import List
from typing import Any

app = FastAPI()
init_db(app)


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    """Тестовый вариант показ юзеров"""
    return await User_Pydantic.from_queryset(User.all())


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@app.post("/division",  response_model=Division_Pydantic)
async def division_add(division: DivisionIn_Pydantic):
    """Добавление Отдела"""
    division_obj = await Division.create(**division.model_dump(exclude_unset=True))
    return await Division_Pydantic.from_tortoise_orm(division_obj)


@app.get("/division/{division_id}")
async def division_get(division_id: int):
    """Поиск отдела по id"""
    return await Division_Pydantic.from_queryset_single(Division.get(id=division_id))


@app.get("/division")
async def division_get():
    """Все отделы"""
    return await Division_Pydantic.from_queryset(Division.all())


@app.post("/create_user", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    """Тестовый вариант добавление юзера"""
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.put("/user/{user_id}", response_model=User_Pydantic)
async def update_user(user_id: int, user: UserIn_Pydantic):
    """Тестовый вариант поиска юзера по id"""
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))
