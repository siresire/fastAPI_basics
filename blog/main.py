from fastapi import FastAPI
from . import schemas,models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()




# Start by creatign a post 
@app.post('/blog')
async def create_blog(request : schemas.Blog):
    return request