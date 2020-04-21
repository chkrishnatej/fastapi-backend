from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

from pydantic import UUID4
from datetime import datetime


class TimestampMixin:
    created_at: datetime = fields.DatetimeField(null=False, auto_now_add=True)
    modified_at: datetime = fields.DatetimeField(null=True, auto_now=True)


class Employee(models.Model, TimestampMixin):
    id: UUID4 = fields.UUIDField(pk=True)
    name: str = fields.CharField(120, null=False)
    username: str = fields.CharField(50, null=False)

    class Meta:
        table = "employee"


Employee_Pydantic = pydantic_model_creator(Employee, name="Employee")
EmployeeIn_Pydantic = pydantic_model_creator(Employee, name="EmployeeIn", exclude_readonly=True)

