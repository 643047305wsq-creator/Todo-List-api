from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base
SQLALCHEMY_DATABASE_URL="sqlite:///./todo.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    completed=Column(Boolean,default=False)
Base.metadata.create_all(bind=engine)