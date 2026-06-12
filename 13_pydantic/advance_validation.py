from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name : str

    @field_validator('first_name', 'last_name')
    def name_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError("First letter must be capital")
        return v
    
class User(BaseModel):
    username: str

    @field_validator('username', mode='before')
    def normalize(cls, v):
        return v.lower().strip()
    
class Product(BaseModel):
    price: str

    @model_validator(mode='after') # type: ignore
    def convert_to_float(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
class DateRange(BaseModel):
    start_time: datetime
    end_time: datetime

    @model_validator(mode='after') # type: ignore
    def validate_date_range(cls, values):
        if values.start_time >= values.end_time:
            raise ValueError("end time must be greater than start time")
        return values