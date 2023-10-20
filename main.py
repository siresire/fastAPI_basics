from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# the model of the data
class Blog(BaseModel):
    title : str
    body  : str
    published : Optional[bool]
    
    
# instance of the fastapi

# base path
# : app is the path operation decorator
# : get is the operation on the path
@app.get("/")
async def index():
    return {"data": {"message": "Welcome to my FastAPI"}}

# base path operation function


# path parameters about 
@app.get("/about")
async def about():
    return {"data": {"message": "About page"}}


# path parameters with dinamic routing 
@app.get("/blog/{id}")
async def show(id : int):
    # fetch blog with id = id
    return {"data": {id} }

# path parameters with dinamic routing 
@app.get("/blog/{id}/comments")
async def comment(id : int ):
    # fetch comment od blog with id = id
    return {"data": "comments" }


# post parameter is used to create something 
# : Blog is the model of the data
@app.post("/blog")
async def create_blog(requests : Blog):
    return {'data': f"blog is created with {requests.dict()}"}