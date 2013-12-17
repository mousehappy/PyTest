from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy import Float
from sqlalchemy import Index, Time, Date
from sqlalchemy.sql import func
from datetime import datetime
sql_engine = create_engine('mysql://root:admin@localhost:3306/MyStock')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, DateTime
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), primary_key=True)
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
    
    
Index("User name index", User.fullname)

class Stock_Management(Base):
    __tablename__ = 'stock_management'
    stock_id = Column(Integer(6), primary_key=True)
    stock_name = Column(String(50), nullable = True)
       

class stock000001(Base):
    __tablename__= '000002'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(Integer)
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('000001_index',stock000001.bigvolumn_status,stock000001.trade_date,stock000001.trade_time)
    

Base.metadata.create_all(sql_engine)

from sqlalchemy.orm import sessionmaker


#Session = sessionmaker(bind=sql_engine)

#session = Session()


#session.add(user1)
#all_users = session.query(User).all()

#print all_users

'''session.add(User('111'))
session.add(User('222', birthday='1985-10-25'))
session.add(User('333', birthday=datetime(1986,11,6)))
session.commit()'''