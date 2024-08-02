from pydantic import BaseModel

class UserUpdate(BaseModel):
    username: str
    mail: str

class UserShow(UserUpdate):
    avatar: str = "https://i.sstatic.net/l60Hf.png"

class User(UserShow):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str