from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user : UserSchema

user = {
        "user": {
            "id": "string",
            "email": "user@example.com",
            "lastName": "string",
            "firstName": "string",
            "middleName": "string"
        }
    }

create_user = CreateUserResponseSchema(**user)
print(create_user)

