from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    postal_code: int

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None
    address: Address

# Mixed nested models

class TextContent(BaseModel):
    type: str = 'text'
    content: str

class ImageContent(BaseModel):
    type: str = 'image'
    url: str

class Blog(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]

# deeply nested models

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Organization(BaseModel):
    name: str
    head_quator: Address
    branches: Optional[List[Address]] = None

