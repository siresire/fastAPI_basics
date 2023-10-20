from fastapi import FastAPI, Depends, status,Response,HTTPException, APIRouter
from .. import schemas,models, database
from sqlalchemy.orm import Session
from typing import List

from .. hashing import Hash

get_db = database.get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
    )


#  Creatign a user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
async def create_user(request : schemas.User, db : Session = Depends(get_db)):
    
    new_user = models.User(name = request.name, email = request.email, password = Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#  get all the user
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
async def all_users(db : Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


#  get a single user
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
async def get_user(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with {id} not found")
    return user