from pydantic import BaseModel
from enum import Enum
from datetime import date

class Seniority(BaseModel):
    ESTAGIARIO = 1
    JUNIOR = 2
    PLENO = 3
    SENIOR = 4
    TECH_LEAD = 5
    N/A = 6

class Position(BaseModel):
    id:int
    name:str
    date_created:date
    is_finished:bool
    customer_id:int

class TechnologyPosition(BaseModel):
    id:int
    technology:str