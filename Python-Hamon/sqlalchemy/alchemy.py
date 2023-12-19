from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,Integer,String,DateTime,create_engine
import datetime
import os
Base = declarative_base()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db ="postgresql:///employee"
engine= create_engine(db,echo=True)
Session = sessionmaker()


"""
class User 
tablename =users
id = pk
usrrname = str
email = str
date = datetime

"""

class User(Base):
    __tablename__='users'
    id = Column(Integer(),primary_key=True)
    username = Column(String(50),nullable=False,unique=True)
    email = Column(String(120),nullable=True,)
    date = Column(DateTime(),default=datetime.date.today())

    def __repr__(self): 
        return f"username={self.username} email={self.email}"


new_user=User(id=1,username="sulaim",email="sulaim@gmail.com")
print(new_user) 

