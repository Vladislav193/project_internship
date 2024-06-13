from fastapi import FastAPI
from app.models import User_Pydantic, UserIn_Pydantic, User, Division
from app.database import init_db
from typing import List
from fastapi import Request
from tortoise.contrib.pydantic import PydanticModel

app = FastAPI()

init_db(app)

# @app.get("/user")
# async def get_user(user: User_Pydantic):
#     user = await user
#     return user
#


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    """Тестовый вариант показ юзеров"""
    return await User_Pydantic.from_queryset(User.all())


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
