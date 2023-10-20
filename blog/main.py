from fastapi import FastAPI, Depends, status,Response,HTTPException
from . import schemas,models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

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
@app.get('/blog', status_code=status.HTTP_200_OK)
async def all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



# Get a single blog
@app.get('/blog{id}', status_code=status.HTTP_200_OK)
async def single_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND, content=f"Blog with {id} not found")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    return blog