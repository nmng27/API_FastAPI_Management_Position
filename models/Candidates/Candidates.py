from pydantic import BaseModel, EmailStr

class Candidate(BaseModel):
    id:int
    name:str
    mail:EmailStr
    phone:str
    age:int
    approved:bool
    position_id:int

class CandidateCreate(BaseModel):
    name:str
    mail:EmailStr
    phone:str
    age:int
    approved:bool
    position_id:int