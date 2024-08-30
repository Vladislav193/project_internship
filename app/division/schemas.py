from tortoise.contrib.pydantic import pydantic_model_creator
from app.division.models import Division
from tortoise import Tortoise



Tortoise.init_models(["app.users.models", "app.division.models"], "models")
Division_Pydantic = pydantic_model_creator(Division, name="Division")
