from fastapi import FastAPI, Query, status, HTTPException
from fastapi.responses import JSONResponse
import random


app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content = {"message":"Hello World"}, status_code = status.HTTP_202_ACCEPTED)

name_list =[ 
{"id":1 ,"name":"ali" },
{"id":2 , "name":"amir"},
{"id":3 , "name":"maryam"}
]




@app.get("/name")
def search_name(q:str|None=None):
    if q:
        return [item for item in name_list if q == item["name"]]
    return name_list

@app.get("/name/{name_id}", status_code = status.HTTP_200_OK)
def retrieve_name_detail(name_id:int):
    for name in name_list:
        if name["id"] == name_id:
            return name
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "object not found")


        

@app.post("/name",status_code = status.HTTP_201_CREATED)
def create_name(name:str):
    name_obj = {"id":random.randint(6,100), "name": name}
    name_list.append(name_obj)
    return name_obj



@app.put("/name/{name_id}")
def update_name_detail(name_id:int, name:str):
    for item in name_list:
        if item["id"]==name_id:
            item["name"] = name
            return item
    return {"detail":"object not found"}


@app.delete("/name/{name_id}")

def delete_name(name_id:int):
    for item in name_list:
        if item["id"]==name_id:
            name_list.remove(item)
            return {"detail":"object deleted succesfully"}
    return {"detail":"object not found"}



