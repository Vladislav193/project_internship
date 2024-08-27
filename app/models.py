from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Division(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    director = fields.CharField(max_length=250)

    def __str__(self):
        return self.director


class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    login = fields.CharField(max_length=250)
    password = fields.CharField(max_length=250)
    email = fields.CharField(max_length=250)
    division = fields.ForeignKeyField('models.Division')
#пример из харба one-to_many
    # division:fields.ForeignKeyField["Division"]

    def __str__(self):
        return self.name




User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn_Pydantic", exclude_readonly=True)
Division_Pydantic = pydantic_model_creator(Division, name="Division")
