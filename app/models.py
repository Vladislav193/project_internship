from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    login = fields.CharField(max_length=250)
    password = fields.CharField(max_length=250)
    email = fields.CharField(max_length=250)
    division = fields.ForeignKeyField('models.Division', related_name='user')

    def __str__(self):
        return self.name


class Division(Model):
    name = fields.CharField(max_length=100)
    director = fields.CharField(max_length=250)

    def __str__(self):
        return self.director


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn_Pydantic", exclude_readonly=True)