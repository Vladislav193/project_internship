from tortoise.models import Model
from tortoise import fields
from app.division.models import Division
# from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    login = fields.CharField(max_length=250)
    password = fields.CharField(max_length=250)
    email = fields.CharField(max_length=250)
    #division = fields.ManyToManyField('models.Division')
    division = fields.ForeignKeyField('models.Division', on_delete=fields.CASCADE, null=True)
#пример из харба one-to_many
    #division: fields.ForeignKeyRelation[Division] = fields.ForeignKeyField('models.Division')
    # division: fields.ForeignKeyRelation["Division"] = fields.ManyToManyField(
    #     "models.Division"
    # )
    def __str__(self):
        return self.name
