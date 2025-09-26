from pydantic import BaseModel
from enum import Enum

class Sector(Enum):
    INDUSTRIA = 1
    SERVICOS = 2
    VAREJO = 3

class Customer(BaseModel):
    id:int
    name:str
    sector:Sector
    is_active:bool

class CustomerCreate(BaseModel):
    name:str
    sector:Sector
    is_active:bool