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

