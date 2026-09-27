from pydantic import BaseModel,field_validator



class PersonBaseSchema(BaseModel):

    name:str

    @field_validator("name")
    def validate_name(cls, value):
        if len(value)>32:
            raise ValueError("name must not exceed 32 caractors")
        if not value.isalpha():
            raise ValueError("Name must contain just Alphacetic caractors")
        return value



class PersonCreateSchema(PersonBaseSchema):
    pass 

class PersonResponeSchema(PersonBaseSchema):
    id : int
    

class PersonUpdateSchema(PersonBaseSchema):
   
   pass