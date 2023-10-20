from fastapi import FastAPI

# instance of the fastapi
app = FastAPI()


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


