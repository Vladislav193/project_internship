from tortoise.models import Model
from tortoise import fields


class Division(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    director = fields.CharField(max_length=250)

    def __str__(self):
        return self.director
