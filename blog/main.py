from fastapi import FastAPI

app = FastAPI()


# Start by creatign a post 
@app.post('/blog')
async def create_blog():
    return "Creating "