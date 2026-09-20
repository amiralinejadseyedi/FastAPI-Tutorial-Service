from pydantic import BaseModel


class PersonCreateSchema(BaseModel):
    name:str 

class PersonResponeSchema(BaseModel):
    id : int
    name : str


class PersonUpdateSchema(BaseModel):
   
    name : str