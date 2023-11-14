from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database,models,myToken

router = APIRouter()

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto" )

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)

@router.post('/login')
def login(request:schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect password")
    
    #access_token =token.create_access_token(data={"sub": user.email})
    
    #return {"access_token": access_token, "token_type" : "bearer"}
    return user