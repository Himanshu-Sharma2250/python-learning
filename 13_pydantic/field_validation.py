from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if (len(v) < 4):
            raise ValueError("Length of username must be greater than 4 characters")
        return v
    
class ResetPassword(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    @classmethod 
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords donot match")
        return values
    
user = User(username="himanshu")
print("User : ", user)

reset = ResetPassword(password='123456789', confirm_password='123456789')
print("New Password : ", reset)