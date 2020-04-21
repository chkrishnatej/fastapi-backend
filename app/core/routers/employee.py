from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.core.models.tortoise.employee import Employee, Employee_Pydantic, EmployeeIn_Pydantic

router = APIRouter()


@router.get("/hello")
def say_hi():
    return JSONResponse("Hi")


@router.post("/create", response_model=Employee_Pydantic,
             description="Create a record for new employee",
             response_description="User created")
async def create_employee(employee: EmployeeIn_Pydantic):
    employee_obj = await Employee.create(**employee.dict(exclude_unset=True))
    return await Employee_Pydantic.from_tortoise_orm(employee_obj)
