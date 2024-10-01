from tortoise.models import Model
from tortoise import fields


class TaskService(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=255)
    employee =  fields.ForeignKeyField('models.User', on_delete=fields.CASCADE)
    task_division = fields.ForeignKeyField('models.Division', on_delete=fields.CASCADE)


    def __str__(self):
        return self.name