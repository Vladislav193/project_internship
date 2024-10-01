from tortoise.contrib.pydantic import pydantic_model_creator
from app.task_service.models import TaskService
from tortoise import Tortoise


Tortoise.init_models(["app.users.models", "app.division.models", "app.task_service.models"], "models")
Task_Pydantic = pydantic_model_creator(TaskService, name="Task_service")
TaskIN_Pydantic = pydantic_model_creator(TaskService, name="TaskIn_Pydantic", exclude_readonly=True)