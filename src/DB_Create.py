from sqlalchemy import create_engine
from sqlalchemy import Sequence
from datetime import datetime
sql_engine = create_engine('mysql://root:admin@localhost:3306/MyStock')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, DateTime
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,  Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50), nullable = True)
    password = Column(String(50), nullable = True)
    birthday = Column(DateTime, default='1970-01-01')
    
    def __init__(self, name, fullname = None, password = None, birthday = None):
        self.name = name
        if fullname != None:
            self.fullname = fullname
        if password != None:
            self.password = password
        if birthday != None:
            self.birthday = birthday
    
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

class Stock_Management(Base):
    __tablename__ = 'stock_management'
    stock_id = Column(Integer(6), primary_key=True)
    stock_name = Column(String(50), nullable = True)
       

#Base.metadata.create_all(sql_engine)

from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=sql_engine)

session = Session()


#session.add(user1)
#all_users = session.query(User).all()

#print all_users

session.add(User('111'))
session.add(User('222', birthday='1985-10-25'))
session.add(User('333', birthday=datetime(1986,11,6)))
session.commit()