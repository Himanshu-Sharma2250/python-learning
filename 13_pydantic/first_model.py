from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# input_data = {
#     "id": 2312,
#     "name": "Himansh",
#     "is_active": 12
# }
# user = User(**input_data)
# gives error : pydantic_core._pydantic_core.ValidationError: 1 validation error for User
# is_active
#   Input should be a valid boolean, unable to interpret input 

input_data = {
    "id": 2312,
    "name": "Himansh",
    "is_active": True
}

# user = User(input_data) # gives error
user = User(**input_data) # ** -> means unpacking just like ... in js to spread the object / dict in python

print(user)

# input_data = {
#     "id": '2312',
#     "name": "Himansh",
#     "is_active": True
# }

# user = User(**input_data) # in this pydantic will try to correct the mistake my converting it in integer and if not able to convert then raise an error