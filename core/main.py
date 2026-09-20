from fastapi import FastAPI, Query, status, HTTPException
from fastapi.responses import JSONResponse
import random
from  dataclasses import dataclass
from schemas import PersonCreateSchema, PersonResponeSchema, PersonUpdateSchema 
from typing import List


app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content = {"message":"Hello World"}, status_code  = status.HTTP_202_ACCEPTED)

name_list =[ 
{"id":1 ,"name":"ali" },
{"id":2 , "name":"amir"},
{"id":3 , "name":"maryam"}
]




@app.get("/name", response_model=List[PersonResponeSchema])
def retrieve_name_list(q : str| None = Query(deprecated=True)):
    if q :
        return [item for item in name_list if q == item["name"]]
    return name_list


@app.get("/name/{name_id}", status_code = status.HTTP_200_OK,response_model = PersonResponeSchema )
def retrieve_name_detail(name_id:int):
    for name in name_list:
        if name["id"] == name_id:
            return name
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "object not found")


@dataclass
class Student:
    name:str
    age:int

@dataclass
class ResponseStudent:
    id:int
    name:str 


              

@app.post("/name",status_code = status.HTTP_201_CREATED, response_model=PersonResponeSchema)
#def create_name(name:str):
def create_name(person : PersonCreateSchema):
    name_obj = {"id":random.randint(6,100), "name": person.name}
    name_list.append(name_obj)
   
    return name_obj



@app.put("/name/{name_id}", response_model=PersonResponeSchema)
def udate_name_detail(name_id:int, person:PersonUpdateSchema):
    for item in name_list:
        if item["id"]==name_id:
            item["name"] = person.name
            return item
    return {"detail":"object not found"}


@app.delete("/name/{name_id}")

def delete_name(name_id:int):
    for item in name_list:
        if item["id"]==name_id:
            name_list.remove(item)
            return {"detail":"object deleted succesfully"}
    return {"detail":"object not found"}



