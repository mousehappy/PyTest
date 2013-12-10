from sqlalchemy import create_engine
from sqlalchemy import Sequence
sql_engine = create_engine('mysql://root:admin@localhost:3306/MyStock')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,  Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
    

Base.metadata.create_all(sql_engine)