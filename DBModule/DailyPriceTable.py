from sqlalchemy import Column, Integer, Sequence, String, Time, Date, Float, DateTime
from sqlalchemy.sql.expression import func
from Modules import G_Base

class DailyPriceTable0(G_Base):
    __tablename__= 'daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable1(G_Base):
    __tablename__= 'daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)   
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable2(G_Base):
    __tablename__= 'daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable3(G_Base):
    __tablename__= 'daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable4(G_Base):
    __tablename__= 'daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable5(G_Base):
    __tablename__= 'daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable6(G_Base):
    __tablename__= 'daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable7(G_Base):
    __tablename__= 'daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable8(G_Base):
    __tablename__= 'daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class DailyPriceTable9(G_Base):
    __tablename__= 'daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable0(G_Base):
    __tablename__= 'sell_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable1(G_Base):
    __tablename__= 'sell_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable2(G_Base):
    __tablename__= 'sell_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable3(G_Base):
    __tablename__= 'sell_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable4(G_Base):
    __tablename__= 'sell_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable5(G_Base):
    __tablename__= 'sell_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable6(G_Base):
    __tablename__= 'sell_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable7(G_Base):
    __tablename__= 'sell_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable8(G_Base):
    __tablename__= 'sell_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellDailyPriceTable9(G_Base):
    __tablename__= 'sell_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable0(G_Base):
    __tablename__= 'buy_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable1(G_Base):
    __tablename__= 'buy_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable2(G_Base):
    __tablename__= 'buy_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable3(G_Base):
    __tablename__= 'buy_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable4(G_Base):
    __tablename__= 'buy_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable5(G_Base):
    __tablename__= 'buy_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable6(G_Base):
    __tablename__= 'buy_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable7(G_Base):
    __tablename__= 'buy_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable8(G_Base):
    __tablename__= 'buy_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyDailyPriceTable9(G_Base):
    __tablename__= 'buy_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())