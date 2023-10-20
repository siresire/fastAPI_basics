from fastapi import FastAPI
from . import models
from .database import engine

from . routers import blog, users, authentication


# migrating all the tables
models.Base.metadata.create_all(bind=engine)



app = FastAPI()


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)
