from sqlalchemy import Column, Sequence
from sqlalchemy.types import Integer, Date, DateTime, String, Time, BigInteger, Numeric
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
            DB_Base.__session_pool = sessionmaker(bind=DB_Base.__engine, expire_on_commit=False)
            return DB_Base.__session_pool()
        if engine != None:
            DB_Base.__engine = create_engine(engine)
            DB_Base.__session_pool = sessionmaker(bind=DB_Base.__engine, expire_on_commit=False)
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
    finance_year = Column(Integer, nullable = True)
    finance_num = Column(Integer, nullable = True)
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
    total_rate = Column(Numeric(10,2))
    tradable_share = Column(BigInteger)
    tradable_rate = Column(Numeric(10,2))
    nontradable_share = Column(BigInteger)
    nontradable_rate = Column(Numeric(10,2))

class StockDailyRecord(G_Base):
    __tablename__= 'stock_daily_record'
    stock_id = Column(String(8), primary_key=True)
    trade_date = Column(Date, primary_key=True)
    init_price = Column(Numeric(10,2))
    end_price = Column(Numeric(10,2))
    high_price = Column(Numeric(10,2))
    low_price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    variat_rate = Column(Numeric(10,2), default = 0)
    amplitude = Column(Numeric(10,2), default = 0)
    trade_amount = Column(Integer)
    trade_count = Column(Integer)
    sell_amount = Column(Integer)
    sell_count = Column(Integer)
    sell_rate = Column(Numeric(10,2), default = 0)
    buy_amount = Column(Integer)
    buy_count = Column(Integer)
    buy_rate = Column(Numeric(10,2), default = 0)
    neutral_amount = Column(Integer)
    neutral_count = Column(Integer)
    neutral_rate = Column(Numeric(10,2), default = 0)
    exchage_rate = Column(Numeric(10,2), default = 0)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class StockFinanceStatement(G_Base):
    __tablename__ = 'stock_finance_statement'
    stock_id = Column(String(8), primary_key = True, autoincrement=False)
    year = Column(Integer, primary_key = True, autoincrement=False)
    type = Column(Integer, primary_key = True, autoincrement=False)
    market = Column(String(4))
    f000 = Column(Numeric(10,2), nullable = True)
    f001 = Column(Numeric(10,2), nullable = True)
    f002 = Column(Numeric(10,2), nullable = True)
    f003 = Column(Numeric(10,2), nullable = True)
    f004 = Column(Numeric(10,2), nullable = True)
    f005 = Column(Numeric(10,2), nullable = True)
    f006 = Column(Numeric(10,2), nullable = True)
    f007 = Column(Numeric(10,2), nullable = True)
    f008 = Column(Numeric(10,2), nullable = True)
    f009 = Column(Numeric(10,2), nullable = True)
    f010 = Column(Numeric(10,2), nullable = True)
    f011 = Column(Numeric(10,2), nullable = True)
    f012 = Column(Numeric(10,2), nullable = True)
    f013 = Column(Numeric(10,2), nullable = True)
    f014 = Column(Numeric(10,2), nullable = True)
    f015 = Column(Numeric(10,2), nullable = True)
    f016 = Column(Numeric(10,2), nullable = True)
    f017 = Column(Numeric(10,2), nullable = True)
    f018 = Column(Numeric(10,2), nullable = True)
    f019 = Column(Numeric(10,2), nullable = True)
    f020 = Column(Numeric(10,2), nullable = True)
    f021 = Column(Numeric(10,2), nullable = True)
    f022 = Column(Numeric(10,2), nullable = True)
    f023 = Column(Numeric(10,2), nullable = True)
    f024 = Column(Numeric(10,2), nullable = True)
    f025 = Column(Numeric(10,2), nullable = True)
    f026 = Column(Numeric(10,2), nullable = True)
    f027 = Column(Numeric(10,2), nullable = True)
    f028 = Column(Numeric(10,2), nullable = True)
    f029 = Column(Numeric(10,2), nullable = True)
    f030 = Column(Numeric(10,2), nullable = True)
    f031 = Column(Numeric(10,2), nullable = True)
    f032 = Column(Numeric(10,2), nullable = True)
    f033 = Column(Numeric(10,2), nullable = True)
    f034 = Column(Numeric(10,2), nullable = True)
    f035 = Column(Numeric(10,2), nullable = True)
    f036 = Column(Numeric(10,2), nullable = True)
    f037 = Column(Numeric(10,2), nullable = True)
    f038 = Column(Numeric(10,2), nullable = True)
    f039 = Column(Numeric(10,2), nullable = True)
    f040 = Column(Numeric(10,2), nullable = True)
    f041 = Column(Numeric(10,2), nullable = True)
    f042 = Column(Numeric(10,2), nullable = True)
    f043 = Column(Numeric(10,2), nullable = True)
    f044 = Column(Numeric(10,2), nullable = True)
    f045 = Column(Numeric(10,2), nullable = True)
    f046 = Column(Numeric(10,2), nullable = True)
    f047 = Column(Numeric(10,2), nullable = True)
    f048 = Column(Numeric(10,2), nullable = True)
    f049 = Column(Numeric(10,2), nullable = True)
    f050 = Column(Numeric(10,2), nullable = True)
    f051 = Column(Numeric(10,2), nullable = True)
    f052 = Column(Numeric(10,2), nullable = True)
    f053 = Column(Numeric(10,2), nullable = True)
    f054 = Column(Numeric(10,2), nullable = True)
    f055 = Column(Numeric(10,2), nullable = True)
    f056 = Column(Numeric(10,2), nullable = True)
    f057 = Column(Numeric(10,2), nullable = True)
    f058 = Column(Numeric(10,2), nullable = True)
    f059 = Column(Numeric(10,2), nullable = True)
    f060 = Column(Numeric(10,2), nullable = True)
    f061 = Column(Numeric(10,2), nullable = True)
    f062 = Column(Numeric(10,2), nullable = True)
    f063 = Column(Numeric(10,2), nullable = True)
    f064 = Column(Numeric(10,2), nullable = True)
    f065 = Column(Numeric(10,2), nullable = True)
    f066 = Column(Numeric(10,2), nullable = True)
    f067 = Column(Numeric(10,2), nullable = True)
    f068 = Column(Numeric(10,2), nullable = True)
    f069 = Column(Numeric(10,2), nullable = True)
    f070 = Column(Numeric(10,2), nullable = True)
    f071 = Column(Numeric(10,2), nullable = True)
    f072 = Column(Numeric(10,2), nullable = True)
    f073 = Column(Numeric(10,2), nullable = True)
    f074 = Column(Numeric(10,2), nullable = True)
    f075 = Column(Numeric(10,2), nullable = True)
    f076 = Column(Numeric(10,2), nullable = True)
    f077 = Column(Numeric(10,2), nullable = True)
    f078 = Column(Numeric(10,2), nullable = True)
    f079 = Column(Numeric(10,2), nullable = True)
    f080 = Column(Numeric(10,2), nullable = True)
    f081 = Column(Numeric(10,2), nullable = True)
    f082 = Column(Numeric(10,2), nullable = True)
    f083 = Column(Numeric(10,2), nullable = True)
    f084 = Column(Numeric(10,2), nullable = True)
    f085 = Column(Numeric(10,2), nullable = True)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
