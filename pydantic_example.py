from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id="fdgfg", name="calicde", email="@email.com")

print(user)