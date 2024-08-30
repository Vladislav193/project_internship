from tortoise.contrib.pydantic import pydantic_model_creator
from app.users.models import User
from tortoise import Tortoise



Tortoise.init_models(["app.users.models", "app.division.models"], "models")
User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn_Pydantic", exclude_readonly=True)

