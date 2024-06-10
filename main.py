from fastapi import FastAPI
from app.models import User_Pydantic, UserIn_Pydantic, User
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
    return await User_Pydantic.from_queryset(User.all())


@app.post("/create_user", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)
