from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    address: Address
    create_at: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={ datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S') }
    ) 

user = User(
    id=1,
    name="himan",
    email="him@fmail.cm",
    is_active=True,
    address=Address( street="some", city="faridabad", postal_code='122222' ),
    create_at=datetime(2026, 6, 12, 15, 1, 5),
    tags=['premium'],
)

print(user)
print("="*100)
print(user.model_dump())
print("="*100)
print(user.model_dump_json())