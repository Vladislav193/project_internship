from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    login = fields.CharField(max_length=250)
    password = fields.CharField(max_length=250)
    email = fields.CharField(max_length=250)
    start_vacation = fields.DateField(null=True)
    finish_vacation = fields.DateField(null=True)
    start_business_trip = fields.DateField(null=True)
    finish_business_trip = fields.DateField(null=True)
    division = fields.ForeignKeyField('models.Division', on_delete=fields.CASCADE, null=True)

    def __str__(self):
        return self.name

