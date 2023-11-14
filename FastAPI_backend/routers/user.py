from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import database,schemas,models,FastAPI_backend.routers.auth as auth

router = APIRouter()

@router.post('/users')
def signup(request: schemas.User,db: Session = Depends(database.get_db)):
    new_user = models.Users(name=request.name, number=request.number, email=request.email,
password=auth.Hash.bcrypt(request.password), subscription=request.subscription)
    db.add (new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/users', response_model=schemas.ShowUser)
def get_user(email : str, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email==email). first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with the email {email} is not available")
    return user