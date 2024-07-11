from pydantic import BaseModel

class User(BaseModel):
    username: str
    mail: str
    password: str
    avatar: str = "https://i.sstatic.net/l60Hf.png"

class UserLogin(BaseModel):
    username: str
    password: str