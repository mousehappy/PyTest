from sqlalchemy import Column, Integer, Sequence, String, Time, Date, Float, DateTime
from sqlalchemy.sql.expression import func
from Modules import G_Base

class BigDailyPriceTable0(G_Base):
    __tablename__= 'big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable1(G_Base):
    __tablename__= 'big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable2(G_Base):
    __tablename__= 'big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable3(G_Base):
    __tablename__= 'big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable4(G_Base):
    __tablename__= 'big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable5(G_Base):
    __tablename__= 'big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    trade_style = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable6(G_Base):
    __tablename__= 'big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable7(G_Base):
    __tablename__= 'big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable8(G_Base):
    __tablename__= 'big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BigDailyPriceTable9(G_Base):
    __tablename__= 'big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable0(G_Base):
    __tablename__= 'sell_big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable1(G_Base):
    __tablename__= 'sell_big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable2(G_Base):
    __tablename__= 'sell_big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable3(G_Base):
    __tablename__= 'sell_big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())


class SellBigDailyPriceTable4(G_Base):
    __tablename__= 'sell_big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable5(G_Base):
    __tablename__= 'sell_big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    trade_style = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable6(G_Base):
    __tablename__= 'sell_big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable7(G_Base):
    __tablename__= 'sell_big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable8(G_Base):
    __tablename__= 'sell_big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class SellBigDailyPriceTable9(G_Base):
    __tablename__= 'sell_big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable0(G_Base):
    __tablename__= 'buy_big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable1(G_Base):
    __tablename__= 'buy_big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable2(G_Base):
    __tablename__= 'buy_big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable3(G_Base):
    __tablename__= 'buy_big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable4(G_Base):
    __tablename__= 'buy_big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable5(G_Base):
    __tablename__= 'buy_big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    trade_style = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable6(G_Base):
    __tablename__= 'buy_big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable7(G_Base):
    __tablename__= 'buy_big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable8(G_Base):
    __tablename__= 'buy_big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    
class BuyBigDailyPriceTable9(G_Base):
    __tablename__= 'buy_big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Float,primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())