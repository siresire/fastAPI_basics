from fastapi import FastAPI

# instance of the fastapi
app = FastAPI()



@app.get("/")
async def index():
    return {"data": {"message": "Welcome to my FastAPI"}}
