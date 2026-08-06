from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base
engine=create_engine("sqlite:///./book.db",connect_args={"check_same_thread":False})
Sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
B=declarative_base()
class Book(B):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    author=Column(String)
    is_read=Column(Boolean,default=False)
B.metadata.create_all(bind=engine)