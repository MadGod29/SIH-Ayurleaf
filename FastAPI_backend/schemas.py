from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name : str
    email : str
    password : str
    subscription : Optional[bool] = False
    number : int

class ShowUser(BaseModel):
    name : str
    email : str
    subscription : bool
    number : int

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str  
    token_type  : str

class TokenData(BaseModel):
    username : Optional[str] = None