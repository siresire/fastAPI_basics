from fastapi import FastAPI, Depends, status,Response,HTTPException
from . import schemas,models
from .database import SessionLocal, engine 
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

from . hashing import Hash




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# migrating all the tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


# Start by creatign a post 
@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create_blog(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#  Delete a blog
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


#  update the blog
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(request : schemas.Blog, id,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'
    



# Get all the blogs
@app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
async def all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



# Get a single blog
@app.get('/blog{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def single_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND, content=f"Blog with {id} not found")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    return blog



#  Creatign a user
@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
async def create_user(request : schemas.User, db : Session = Depends(get_db)):
    
    new_user = models.User(name = request.name, email = request.email, password = Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#  get all the user
@app.get('/user', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
async def all_users(db : Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users