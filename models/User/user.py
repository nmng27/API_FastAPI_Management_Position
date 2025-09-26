from pydantic import BaseModel
from datetime import date
from enum import Enum

class Role(Enum):
    ADMIN = 1
    USER = 2


class User(BaseModel):
    id:int
    name:str
    email:str
    date_birth:date
    role:Role
    passwordWithHash:str