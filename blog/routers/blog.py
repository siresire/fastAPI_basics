from fastapi import FastAPI, Depends, status,Response,HTTPException, APIRouter
from .. import schemas,models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
# from ..oauth2 import oauth2

get_db = database.get_db

router = APIRouter(
    prefix='/blog',
    tags=['blogs'])



# Get all the blogs
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
async def all_blogs(db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
   


# Get a single blog
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def single_blog(id, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.single_blog(id, db)
    

# creatign a post 
@router.post('/', status_code=status.HTTP_201_CREATED, tags=['blogs'])
async def create_blog(request : schemas.Blog, db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

#  Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)



#  update the blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(request : schemas.Blog, id,db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    
    
    return blog.update(request, id, db)
    



