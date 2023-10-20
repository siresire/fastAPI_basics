from fastapi import FastAPI

from . import schemas


app = FastAPI()




# Start by creatign a post 
@app.post('/blog')
async def create_blog(request : schemas.Blog):
    return request