from fastapi import FastAPI, Depends, status,Response,HTTPException, APIRouter
from .. import schemas,models, database
from sqlalchemy.orm import Session
from typing import List

get_db = database.get_db

router = APIRouter(
    prefix='/blog',
    tags=['blogs'])



# Get all the blogs
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
async def all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Get a single blog
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def single_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND, content=f"Blog with {id} not found")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    return blog

# creatign a post 
@router.post('/', status_code=status.HTTP_201_CREATED, tags=['blogs'])
async def create_blog(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#  Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'



#  update the blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(request : schemas.Blog, id,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'
    


