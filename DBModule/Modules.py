from sqlalchemy import Column, Sequence
from sqlalchemy.types import Integer, Date, DateTime, String, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.schema import Index

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
    id = Column(String(8), primary_key=True)
    name = Column(String(30))
    status = Column(Integer, default = 0)
    data_begin_date = Column(Date, nullable = True)
    data_end_date = Column(Date, nullable = True)
    processed_date = Column(Date, nullable = True)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    update_timestamp = Column(DateTime, nullable = True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return "<Stock(id='%s', name='%s',status='%s','last_crawl_date'='%s')>" % (self.id, self.name, self.status, self.data_end_date)

class stocktbl0(__Base):
    __tablename__= 'stocktbl0'
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
    
Index('stocktbl0_index',stocktbl0.bigvolumn_status,stocktbl0.trade_date,stocktbl0.trade_time)

class stocktbl1(__Base):
    __tablename__= 'stocktbl1'
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
    
Index('stocktbl1_index',stocktbl1.bigvolumn_status,stocktbl1.trade_date,stocktbl1.trade_time)
    
class stocktbl2(__Base):
    __tablename__= 'stocktbl2'
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
    
Index('stocktbl2_index',stocktbl2.bigvolumn_status,stocktbl2.trade_date,stocktbl2.trade_time)
    
class stocktbl3(__Base):
    __tablename__= 'stocktbl3'
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
    
Index('stocktbl3_index',stocktbl3.bigvolumn_status,stocktbl3.trade_date,stocktbl3.trade_time)
    
class stocktbl4(__Base):
    __tablename__= 'stocktbl4'
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
    
Index('stocktbl4_index',stocktbl4.bigvolumn_status,stocktbl4.trade_date,stocktbl4.trade_time)
    
class stocktbl5(__Base):
    __tablename__= 'stocktbl5'
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
    
Index('stocktbl5_index',stocktbl5.bigvolumn_status,stocktbl5.trade_date,stocktbl5.trade_time)
    
class stocktbl6(__Base):
    __tablename__= 'stocktbl6'
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
    
Index('stocktbl6_index',stocktbl6.bigvolumn_status,stocktbl6.trade_date,stocktbl6.trade_time)
    
class stocktbl7(__Base):
    __tablename__= 'stocktbl7'
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
    
Index('stocktbl7_index',stocktbl7.bigvolumn_status,stocktbl7.trade_date,stocktbl7.trade_time)
    
class stocktbl8(__Base):
    __tablename__= 'stocktbl8'
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
    
Index('stocktbl8_index',stocktbl8.bigvolumn_status,stocktbl8.trade_date,stocktbl8.trade_time)
    
class stocktbl9(__Base):
    __tablename__= 'stocktbl9'
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
    
Index('stocktbl9_index',stocktbl9.bigvolumn_status,stocktbl9.trade_date,stocktbl9.trade_time)


