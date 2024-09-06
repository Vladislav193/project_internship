from tortoise.models import Model
from tortoise import fields
# from tortoise.validators import Validator
# from tortoise.exceptions import ValidationError
# from pydantic import field_validator


# class ValidatorVacation(Validator):
#     t = []
#     def __call__(self, v1):
#         self.t.append(v1)
#         print(self.t)
#         # if not value:
#         #     raise ValidationError(f"Value can not be empty")

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


    # @field_validator("start_business_trip")
    # @classmethod
    # def validator_vacation(cls, value):
    #     print(cls.value)
    #     if value.start_vacation is not None and value.start_vacation <= value.start_business_trip:
    #         raise ValueError("командировка не мождет пересекаться с отпуском")
    #     return value
