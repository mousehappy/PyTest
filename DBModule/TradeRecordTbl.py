from sqlalchemy import Column, Integer, Sequence, String, Time, Date, Numeric, DateTime
from Modules import G_Base
from sqlalchemy.sql.expression import func
from sqlalchemy.schema import Index, ForeignKey

class stocktbl0(G_Base):
    __tablename__= 'stocktbl0'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
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
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl9_index',stocktbl9.stock_id,stocktbl9.bigvolumn_status,stocktbl9.trade_date,stocktbl9.trade_time)

class stocktbl10(G_Base):
    __tablename__= 'stocktbl10'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl10_index',stocktbl10.stock_id,stocktbl10.bigvolumn_status,stocktbl10.trade_date,stocktbl10.trade_time)

class stocktbl11(G_Base):
    __tablename__= 'stocktbl11'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl11_index',stocktbl11.stock_id,stocktbl11.bigvolumn_status,stocktbl11.trade_date,stocktbl11.trade_time)

class stocktbl12(G_Base):
    __tablename__= 'stocktbl12'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl12_index',stocktbl12.stock_id,stocktbl12.bigvolumn_status,stocktbl12.trade_date,stocktbl12.trade_time)

class stocktbl13(G_Base):
    __tablename__= 'stocktbl13'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl13_index',stocktbl13.stock_id,stocktbl13.bigvolumn_status,stocktbl13.trade_date,stocktbl13.trade_time)

class stocktbl14(G_Base):
    __tablename__= 'stocktbl14'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl14_index',stocktbl14.stock_id,stocktbl14.bigvolumn_status,stocktbl14.trade_date,stocktbl14.trade_time)

class stocktbl15(G_Base):
    __tablename__= 'stocktbl15'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl15_index',stocktbl15.stock_id,stocktbl15.bigvolumn_status,stocktbl15.trade_date,stocktbl15.trade_time)

class stocktbl16(G_Base):
    __tablename__= 'stocktbl16'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl16_index',stocktbl16.stock_id,stocktbl16.bigvolumn_status,stocktbl16.trade_date,stocktbl16.trade_time)

class stocktbl17(G_Base):
    __tablename__= 'stocktbl17'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl17_index',stocktbl17.stock_id,stocktbl17.bigvolumn_status,stocktbl17.trade_date,stocktbl17.trade_time)

class stocktbl18(G_Base):
    __tablename__= 'stocktbl18'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl18_index',stocktbl18.stock_id,stocktbl18.bigvolumn_status,stocktbl18.trade_date,stocktbl18.trade_time)

class stocktbl19(G_Base):
    __tablename__= 'stocktbl19'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl19_index',stocktbl19.stock_id,stocktbl19.bigvolumn_status,stocktbl19.trade_date,stocktbl19.trade_time)

class stocktbl20(G_Base):
    __tablename__= 'stocktbl20'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl20_index',stocktbl20.stock_id,stocktbl20.bigvolumn_status,stocktbl20.trade_date,stocktbl20.trade_time)

class stocktbl21(G_Base):
    __tablename__= 'stocktbl21'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl21_index',stocktbl21.stock_id,stocktbl21.bigvolumn_status,stocktbl21.trade_date,stocktbl21.trade_time)

class stocktbl22(G_Base):
    __tablename__= 'stocktbl22'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl22_index',stocktbl22.stock_id,stocktbl22.bigvolumn_status,stocktbl22.trade_date,stocktbl22.trade_time)

class stocktbl23(G_Base):
    __tablename__= 'stocktbl23'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl23_index',stocktbl23.stock_id,stocktbl23.bigvolumn_status,stocktbl23.trade_date,stocktbl23.trade_time)

class stocktbl24(G_Base):
    __tablename__= 'stocktbl24'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl24_index',stocktbl24.stock_id,stocktbl24.bigvolumn_status,stocktbl24.trade_date,stocktbl24.trade_time)

class stocktbl25(G_Base):
    __tablename__= 'stocktbl25'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl25_index',stocktbl25.stock_id,stocktbl25.bigvolumn_status,stocktbl25.trade_date,stocktbl25.trade_time)

class stocktbl26(G_Base):
    __tablename__= 'stocktbl26'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl26_index',stocktbl26.stock_id,stocktbl26.bigvolumn_status,stocktbl26.trade_date,stocktbl26.trade_time)

class stocktbl27(G_Base):
    __tablename__= 'stocktbl27'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl27_index',stocktbl27.stock_id,stocktbl27.bigvolumn_status,stocktbl27.trade_date,stocktbl27.trade_time)

class stocktbl28(G_Base):
    __tablename__= 'stocktbl28'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl28_index',stocktbl28.stock_id,stocktbl28.bigvolumn_status,stocktbl28.trade_date,stocktbl28.trade_time)

class stocktbl29(G_Base):
    __tablename__= 'stocktbl29'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl29_index',stocktbl29.stock_id,stocktbl29.bigvolumn_status,stocktbl29.trade_date,stocktbl29.trade_time)

class stocktbl30(G_Base):
    __tablename__= 'stocktbl30'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl30_index',stocktbl30.stock_id,stocktbl30.bigvolumn_status,stocktbl30.trade_date,stocktbl30.trade_time)

class stocktbl31(G_Base):
    __tablename__= 'stocktbl31'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl31_index',stocktbl31.stock_id,stocktbl31.bigvolumn_status,stocktbl31.trade_date,stocktbl31.trade_time)

class stocktbl32(G_Base):
    __tablename__= 'stocktbl32'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl32_index',stocktbl32.stock_id,stocktbl32.bigvolumn_status,stocktbl32.trade_date,stocktbl32.trade_time)

class stocktbl33(G_Base):
    __tablename__= 'stocktbl33'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl33_index',stocktbl33.stock_id,stocktbl33.bigvolumn_status,stocktbl33.trade_date,stocktbl33.trade_time)

class stocktbl34(G_Base):
    __tablename__= 'stocktbl34'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl34_index',stocktbl34.stock_id,stocktbl34.bigvolumn_status,stocktbl34.trade_date,stocktbl34.trade_time)

class stocktbl35(G_Base):
    __tablename__= 'stocktbl35'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl35_index',stocktbl35.stock_id,stocktbl35.bigvolumn_status,stocktbl35.trade_date,stocktbl35.trade_time)

class stocktbl36(G_Base):
    __tablename__= 'stocktbl36'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl36_index',stocktbl36.stock_id,stocktbl36.bigvolumn_status,stocktbl36.trade_date,stocktbl36.trade_time)

class stocktbl37(G_Base):
    __tablename__= 'stocktbl37'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl37_index',stocktbl37.stock_id,stocktbl37.bigvolumn_status,stocktbl37.trade_date,stocktbl37.trade_time)

class stocktbl38(G_Base):
    __tablename__= 'stocktbl38'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl38_index',stocktbl38.stock_id,stocktbl38.bigvolumn_status,stocktbl38.trade_date,stocktbl38.trade_time)

class stocktbl39(G_Base):
    __tablename__= 'stocktbl39'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl39_index',stocktbl39.stock_id,stocktbl39.bigvolumn_status,stocktbl39.trade_date,stocktbl39.trade_time)

class stocktbl40(G_Base):
    __tablename__= 'stocktbl40'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl40_index',stocktbl40.stock_id,stocktbl40.bigvolumn_status,stocktbl40.trade_date,stocktbl40.trade_time)

class stocktbl41(G_Base):
    __tablename__= 'stocktbl41'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl41_index',stocktbl41.stock_id,stocktbl41.bigvolumn_status,stocktbl41.trade_date,stocktbl41.trade_time)

class stocktbl42(G_Base):
    __tablename__= 'stocktbl42'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl42_index',stocktbl42.stock_id,stocktbl42.bigvolumn_status,stocktbl42.trade_date,stocktbl42.trade_time)

class stocktbl43(G_Base):
    __tablename__= 'stocktbl43'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl43_index',stocktbl43.stock_id,stocktbl43.bigvolumn_status,stocktbl43.trade_date,stocktbl43.trade_time)

class stocktbl44(G_Base):
    __tablename__= 'stocktbl44'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl44_index',stocktbl44.stock_id,stocktbl44.bigvolumn_status,stocktbl44.trade_date,stocktbl44.trade_time)

class stocktbl45(G_Base):
    __tablename__= 'stocktbl45'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl45_index',stocktbl45.stock_id,stocktbl45.bigvolumn_status,stocktbl45.trade_date,stocktbl45.trade_time)

class stocktbl46(G_Base):
    __tablename__= 'stocktbl46'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl46_index',stocktbl46.stock_id,stocktbl46.bigvolumn_status,stocktbl46.trade_date,stocktbl46.trade_time)

class stocktbl47(G_Base):
    __tablename__= 'stocktbl47'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl47_index',stocktbl47.stock_id,stocktbl47.bigvolumn_status,stocktbl47.trade_date,stocktbl47.trade_time)

class stocktbl48(G_Base):
    __tablename__= 'stocktbl48'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl48_index',stocktbl48.stock_id,stocktbl48.bigvolumn_status,stocktbl48.trade_date,stocktbl48.trade_time)

class stocktbl49(G_Base):
    __tablename__= 'stocktbl49'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True, unique=True)
    stock_id = Column(String(8))
    bigvolumn_status = Column(Integer)
    trade_time = Column(Time)
    trade_date = Column(Date)
    price = Column(Numeric(10,2))
    variation = Column(Numeric(10,2), default = 0)
    trade_volumn = Column(Integer)
    trade_value = Column(Numeric(10,2))
    trade_status = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
Index('stocktbl49_index',stocktbl49.stock_id,stocktbl49.bigvolumn_status,stocktbl49.trade_date,stocktbl49.trade_time)