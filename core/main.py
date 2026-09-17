from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

name_list =[ 
{"id":1 ,"name":"ali" },
{"id":2 , "name":"amir"},
{"id":3 , "name":"maryam"}
]


@app.get("/name")
def retrieve_name_list():
    return name_list


@app.get("/name/{name_id}")
def retrieve_name_detail(name_id:int):
    for name in name_list:
        if name["id"] == name_id:
            return name
    return {"detail":"object not found"}
