from database import Base
from sqlalchemy import Column,Integer,String,Boolean

class Users(Base):
    __tablename__ = 'Users'
    
    name = Column(String,primary_key=True)
    number = Column(Integer)
    email = Column(String)
    password = Column(String)
    subscription = Column(Boolean)
