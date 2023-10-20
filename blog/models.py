from sqlalchemy import Column, Integer, String
from . database import Base


class Blog(Base):
    
    # model connected to table called blogs
    __tablename__ = "blogs"
    
    
    # fileds of the table blogs
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    body = Column(String)