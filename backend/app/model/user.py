from pydantic import BaseModel

class UserShow(BaseModel):
    username: str
    mail: str
    avatar: str = "https://i.sstatic.net/l60Hf.png"

class User(UserShow):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str