from sqlalchemy import Column, Sequence
from sqlalchemy.types import Integer, Date, DateTime, String, Time, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.schema import Index, ForeignKey
from Crawler.CrawlConfig import G_Config

class DB_Base:
    G_Base = declarative_base()
    __engine = None
    __session_pool = None
    def __init__(self, engine=None, config=None):
        if DB_Base.__engine != None:
            print "Database engine already exists"
            return
        if engine != None:
            DB_Base.__engine = create_engine(engine,**config)
            
    def get_engine(self, engine = None):
        if DB_Base.__engine != None:
            return DB_Base.__engine
        if engine != None:
            DB_Base.__engine = create_engine(engine)
            return DB_Base.__engine
        print "You need input your engine!!!"
    
    def get_base(self):
        return DB_Base.G_Base
    
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


        
    



G_DB = DB_Base(G_Config.db_str, G_Config.db_args)

G_Base = G_DB.get_base()

class StockManagement(G_Base):
    __tablename__= 'stock_management'
    id = Column(String(8), primary_key=True)
    market = Column(String(4), nullable = True)
    name = Column(String(30), nullable = True)
    status = Column(Integer, default = 0)
    data_begin_date = Column(Date, nullable = True)
    data_end_date = Column(Date, nullable = True)
    processed_date = Column(Date, nullable = True)
    finace_date = Column(String(10), nullable = True)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    update_timestamp = Column(DateTime, nullable = True)
    
    def __init__(self, id = None, name = None):
        if id:
            self.id = id
        if name:
            self.name = name
        
    def __repr__(self):
        return "<Stock(id='%s', name='%s',status='%s','last_crawl_date'='%s')>" % (self.id, self.name, self.status, self.data_end_date)
    
class CSRCCategory(G_Base):
    __tablename__='csrc_category'
    id = Column(Integer, Sequence('csrc_id_seq'), unique=True)
    name = Column(String(20), primary_key=True, unique=True)
    cate_type = Column(Integer, default = 0)
    parent_cate = Column(Integer, default = 0)
    
class SSECategory(G_Base):
    __tablename__='sse_category'
    id = Column(Integer, Sequence('sse_id_seq'), unique=True)
    name = Column(String(20), primary_key=True, unique=True)
    
class StockBaseInfo(G_Base):
    __tablename__='stock_base_info'
    id = Column(String(8), primary_key=True)
    name = Column(String(30), nullable = True)
    area = Column(String(4))
    Astatus = Column(String(8))
    Bstatus = Column(String(8), nullable = True)
    IPODate = Column(Date, nullable = True)
    csrc_main_cate = Column(Integer, ForeignKey('csrc_category.id'), nullable = True)
    csrc_mid_cate = Column(Integer, ForeignKey('csrc_category.id'), nullable = True)
    csrc_sub_cate = Column(Integer, ForeignKey('csrc_category.id'), nullable = True)
    sse_cate = Column(Integer, ForeignKey('sse_category.id'), nullable = True)
    total_share = Column(BigInteger)
    total_rate = Column(Float)
    tradable_share = Column(BigInteger)
    tradable_rate = Column(Float)
    nontradable_share = Column(BigInteger)
    nontradable_rate = Column(Float)

class StockDailyRecord(G_Base):
    __tablename__= 'stock_daily_record'
    stock_id = Column(String(8), primary_key=True)
    trade_date = Column(Date, primary_key=True)
    init_price = Column(Float)
    end_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    variation = Column(Float, default = 0)
    variat_rate = Column(Float, default = 0)
    amplitude = Column(Float, default = 0)
    trade_amount = Column(Integer)
    trade_count = Column(Integer)
    sell_amount = Column(Integer)
    sell_count = Column(Integer)
    sell_rate = Column(Float, default = 0)
    buy_amount = Column(Integer)
    buy_count = Column(Integer)
    buy_rate = Column(Float, default = 0)
    neutral_amount = Column(Integer)
    neutral_count = Column(Integer)
    neutral_rate = Column(Float, default = 0)
    exchage_rate = Column(Float, default = 0)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class stocktbl0(G_Base):
    __tablename__= 'stocktbl0'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl0_index',stocktbl0.stock_id,stocktbl0.bigvolumn_status,stocktbl0.trade_date,stocktbl0.trade_time)

class stocktbl1(G_Base):
    __tablename__= 'stocktbl1'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl1_index',stocktbl1.stock_id,stocktbl1.bigvolumn_status,stocktbl1.trade_date,stocktbl1.trade_time)
    
class stocktbl2(G_Base):
    __tablename__= 'stocktbl2'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl2_index',stocktbl2.stock_id,stocktbl2.bigvolumn_status,stocktbl2.trade_date,stocktbl2.trade_time)
    
class stocktbl3(G_Base):
    __tablename__= 'stocktbl3'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl3_index',stocktbl3.stock_id,stocktbl3.bigvolumn_status,stocktbl3.trade_date,stocktbl3.trade_time)
    
class stocktbl4(G_Base):
    __tablename__= 'stocktbl4'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl4_index',stocktbl4.stock_id,stocktbl4.bigvolumn_status,stocktbl4.trade_date,stocktbl4.trade_time)
    
class stocktbl5(G_Base):
    __tablename__= 'stocktbl5'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl5_index',stocktbl5.stock_id,stocktbl5.bigvolumn_status,stocktbl5.trade_date,stocktbl5.trade_time)
    
class stocktbl6(G_Base):
    __tablename__= 'stocktbl6'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl6_index',stocktbl6.stock_id,stocktbl6.bigvolumn_status,stocktbl6.trade_date,stocktbl6.trade_time)
    
class stocktbl7(G_Base):
    __tablename__= 'stocktbl7'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl7_index',stocktbl7.stock_id,stocktbl7.bigvolumn_status,stocktbl7.trade_date,stocktbl7.trade_time)
    
class stocktbl8(G_Base):
    __tablename__= 'stocktbl8'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl8_index',stocktbl8.stock_id,stocktbl8.bigvolumn_status,stocktbl8.trade_date,stocktbl8.trade_time)
    
class stocktbl9(G_Base):
    __tablename__= 'stocktbl9'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Float)
    variation = Column(Float, default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Float)
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl9_index',stocktbl9.stock_id, stocktbl9.bigvolumn_status,stocktbl9.trade_date,stocktbl9.trade_time)


