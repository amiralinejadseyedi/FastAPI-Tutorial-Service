from fastapi import FastAPI, Query, status, HTTPException, Depends
from fastapi.responses import JSONResponse
import random
from  dataclasses import dataclass
from schemas import PersonBaseSchema, PersonCreateSchema, PersonResponeSchema, PersonUpdateSchema 
from typing import List
from database import Base, engine, get_db, Person
from sqlalchemy.orm import Session 


Base.metadata.create_all(engine)



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
def retrieve_name_list(q : str| None = Query(deprecated=True), db:Session = Depends(get_db) ):
    query = db.query(Person)
    if  q:
        query = query.filter_by(name=q)
    result = query.all()
    #if q :
    #    return [item for item in name_list if q == item["name"]]
    return result

 
@app.get("/name/{name_id}", status_code = status.HTTP_200_OK,response_model = PersonResponeSchema )
def retrieve_name_detail(name_id:int, db:Session = Depends(get_db) ):
    #for name in name_list:
    #    if name["id"] == name_id:
    #        return name

    person = db.query(Person).filter_by(id = name_id).one_or_none()
    if person:
        return person
    else:
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
def create_name(request : PersonCreateSchema, db:Session = Depends(get_db)):
   # name_obj = {"id":random.randint(6,100), "name": person.name}
   # name_list.append(name_obj)
    new_person = Person(name= request.name)
    db.add(new_person)
    db.commit() 
    db.refresh(new_person)
    return new_person



@app.put("/name/{name_id}", response_model=PersonResponeSchema)
def udate_name_detail(name_id:int, request:PersonUpdateSchema,db:Session = Depends(get_db) ):
   # for item in name_list:
    #    if item["id"]==name_id:
     #       item["name"] = person.name
      #      return item
    #return {"detail":"object not found"}
    
    person = db.query(Person).filter_by(id = name_id).one_or_none()
    if person:
        print(person)
        person.name = request.name
        db.commit()
        db.refresh(person)
        return person
    else:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "object not found")   



@app.delete("/name/{name_id}")

def delete_name(name_id:int, db:Session = Depends(get_db) ):
   # for item in name_list:
   #     if item["id"]==name_id:
   #         name_list.remove(item)
   #         return {"detail":"object deleted succesfully"}
   # return {"detail":"object not found"}

    person = db.query(Person).filter_by(id = name_id).one_or_none()
    if person:
        db.delete(person)
        db.commit()
        return {"detail":"object deleted succesfully"}
    else:
        return {"detail":"object not found"}

