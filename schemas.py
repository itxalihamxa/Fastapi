from datetime import datetime
from pydantic import BaseModel



class Postschemas(BaseModel):
    id: int
    title: str
    content: str
    published: bool

class post(Postschemas):
    class Config:
        orm_mode = True


class Userschemas(BaseModel):
    id: int
    username: str
    email: str
    password: str

class User(BaseModel):

    email: str
    password: str
    class Config:
        orm_mode = True