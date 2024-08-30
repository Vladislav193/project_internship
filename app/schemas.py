from tortoise.contrib.pydantic import pydantic_model_creator
from models import User, Division




User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn_Pydantic", exclude_readonly=True)
Division_Pydantic = pydantic_model_creator(Division, name="Division")
