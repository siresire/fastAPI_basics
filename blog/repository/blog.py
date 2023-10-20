from ..import models ,schemas
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status,Response,HTTPException, APIRouter

def get_all(db: Session):
     blogs = db.query(models.Blog).all()
     return  blogs
 
 
def create(request, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(request : schemas.Blog, id:int,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'
    

def single_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND, content=f"Blog with {id} not found")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    return blog


     
    