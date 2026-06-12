from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: int

class User(BaseModel):
    id: int
    name: str
    address: Address

user_data = {
    "id": 123,
    "name": "Jitesh",
    "address": {
        "street": "7, Hanuman Nagar",
        "city": "Faridabad",
        "postal_code": 121002
    }
}

user = User(**user_data)

print(user)