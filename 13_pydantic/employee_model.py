from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        examples=["Himanshu Sharma"],
    )
    department: Optional[str]
    salary: float = Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email: str = Field(..., description="Email of user")
    phone: str = Field(...,)
    age: int = Field(..., le=150, ge=0)

employee_data = {
    "id": 2323,
    "name": "Ajay",
    "department": "Engineering",
    "salary": 23000
}

employee = Employee(**employee_data)

print("employee: ", employee)