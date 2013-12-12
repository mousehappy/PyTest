from sqlalchemy import Column, Integer, Date, DateTime, String, TIMESTAMP, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

class DB_Base:
    __base = declarative_base()
    __engine = None
    __session_pool = None
    def __init__(self, engine=None):
        if DB_Base.__engine != None:
            print "Database engine already exists"
            return
        if engine != None:
            DB_Base.__engine = create_engine(engine)
            
    def get_engine(self, engine = None):
        if DB_Base.__engine != None:
            return DB_Base.__engine
        if engine != None:
            DB_Base.__engine = create_engine(engine)
            return DB_Base.__engine
        print "You need input your engine!!!"
    
    def get_base(self):
        return DB_Base.__base
    
    def get_session(self, engine = None):
        if DB_Base.__session_pool != None:
            return DB_Base.__session_pool()
        if DB_Base.__engine != None:
            DB_Base.__session_pool = sessionmaker(bind=DB_Base.__engine)
            return DB_Base.__session_pool()
        if engine != None:
            DB_Base.__engine = create_engine(engine)
            DB_Base.__session_pool = sessionmaker(bind=DB_Base.__engine)
            return DB_Base.__session_pool()
        print "Need an engine first!!!"

            
        
    

__DB = DB_Base()

__Base = __DB.get_base()

class StockManagement(__Base):
    __tablename__= 'stock_management'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    status = Column(Integer, default = 0)
    data_begin_date = Column(Date, nullable = True)
    data_end_date = Column(Date, nullable = True)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    update_timestamp = Column(DateTime, nullable = True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return "<Stock(id='%s', name='%s',status='%s','last_crawl_date'='%s')>" % (self.id, self.name, self.status, self.date_end_date)

