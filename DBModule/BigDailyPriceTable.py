from sqlalchemy import Column, Integer, Sequence, String, Time, Date, Numeric, DateTime
from sqlalchemy.sql.expression import func
from Modules import G_Base

class BigDailyPriceTable0(G_Base):
    __tablename__= 'big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable0(G_Base):
    __tablename__= 'buy_big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable0(G_Base):
    __tablename__= 'sell_big_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable1(G_Base):
    __tablename__= 'big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable1(G_Base):
    __tablename__= 'buy_big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable1(G_Base):
    __tablename__= 'sell_big_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable2(G_Base):
    __tablename__= 'big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable2(G_Base):
    __tablename__= 'buy_big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable2(G_Base):
    __tablename__= 'sell_big_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable3(G_Base):
    __tablename__= 'big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable3(G_Base):
    __tablename__= 'buy_big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable3(G_Base):
    __tablename__= 'sell_big_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable4(G_Base):
    __tablename__= 'big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable4(G_Base):
    __tablename__= 'buy_big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable4(G_Base):
    __tablename__= 'sell_big_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable5(G_Base):
    __tablename__= 'big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable5(G_Base):
    __tablename__= 'buy_big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable5(G_Base):
    __tablename__= 'sell_big_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable6(G_Base):
    __tablename__= 'big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable6(G_Base):
    __tablename__= 'buy_big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable6(G_Base):
    __tablename__= 'sell_big_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable7(G_Base):
    __tablename__= 'big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable7(G_Base):
    __tablename__= 'buy_big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable7(G_Base):
    __tablename__= 'sell_big_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable8(G_Base):
    __tablename__= 'big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable8(G_Base):
    __tablename__= 'buy_big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable8(G_Base):
    __tablename__= 'sell_big_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable9(G_Base):
    __tablename__= 'big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable9(G_Base):
    __tablename__= 'buy_big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable9(G_Base):
    __tablename__= 'sell_big_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable10(G_Base):
    __tablename__= 'big_daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable10(G_Base):
    __tablename__= 'buy_big_daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable10(G_Base):
    __tablename__= 'sell_big_daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable11(G_Base):
    __tablename__= 'big_daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable11(G_Base):
    __tablename__= 'buy_big_daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable11(G_Base):
    __tablename__= 'sell_big_daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable12(G_Base):
    __tablename__= 'big_daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable12(G_Base):
    __tablename__= 'buy_big_daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable12(G_Base):
    __tablename__= 'sell_big_daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable13(G_Base):
    __tablename__= 'big_daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable13(G_Base):
    __tablename__= 'buy_big_daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable13(G_Base):
    __tablename__= 'sell_big_daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable14(G_Base):
    __tablename__= 'big_daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable14(G_Base):
    __tablename__= 'buy_big_daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable14(G_Base):
    __tablename__= 'sell_big_daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable15(G_Base):
    __tablename__= 'big_daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable15(G_Base):
    __tablename__= 'buy_big_daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable15(G_Base):
    __tablename__= 'sell_big_daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable16(G_Base):
    __tablename__= 'big_daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable16(G_Base):
    __tablename__= 'buy_big_daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable16(G_Base):
    __tablename__= 'sell_big_daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable17(G_Base):
    __tablename__= 'big_daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable17(G_Base):
    __tablename__= 'buy_big_daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable17(G_Base):
    __tablename__= 'sell_big_daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable18(G_Base):
    __tablename__= 'big_daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable18(G_Base):
    __tablename__= 'buy_big_daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable18(G_Base):
    __tablename__= 'sell_big_daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable19(G_Base):
    __tablename__= 'big_daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable19(G_Base):
    __tablename__= 'buy_big_daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable19(G_Base):
    __tablename__= 'sell_big_daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable20(G_Base):
    __tablename__= 'big_daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable20(G_Base):
    __tablename__= 'buy_big_daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable20(G_Base):
    __tablename__= 'sell_big_daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable21(G_Base):
    __tablename__= 'big_daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable21(G_Base):
    __tablename__= 'buy_big_daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable21(G_Base):
    __tablename__= 'sell_big_daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable22(G_Base):
    __tablename__= 'big_daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable22(G_Base):
    __tablename__= 'buy_big_daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable22(G_Base):
    __tablename__= 'sell_big_daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable23(G_Base):
    __tablename__= 'big_daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable23(G_Base):
    __tablename__= 'buy_big_daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable23(G_Base):
    __tablename__= 'sell_big_daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable24(G_Base):
    __tablename__= 'big_daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable24(G_Base):
    __tablename__= 'buy_big_daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable24(G_Base):
    __tablename__= 'sell_big_daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable25(G_Base):
    __tablename__= 'big_daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable25(G_Base):
    __tablename__= 'buy_big_daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable25(G_Base):
    __tablename__= 'sell_big_daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable26(G_Base):
    __tablename__= 'big_daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable26(G_Base):
    __tablename__= 'buy_big_daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable26(G_Base):
    __tablename__= 'sell_big_daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable27(G_Base):
    __tablename__= 'big_daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable27(G_Base):
    __tablename__= 'buy_big_daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable27(G_Base):
    __tablename__= 'sell_big_daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable28(G_Base):
    __tablename__= 'big_daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable28(G_Base):
    __tablename__= 'buy_big_daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable28(G_Base):
    __tablename__= 'sell_big_daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable29(G_Base):
    __tablename__= 'big_daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable29(G_Base):
    __tablename__= 'buy_big_daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable29(G_Base):
    __tablename__= 'sell_big_daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable30(G_Base):
    __tablename__= 'big_daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable30(G_Base):
    __tablename__= 'buy_big_daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable30(G_Base):
    __tablename__= 'sell_big_daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable31(G_Base):
    __tablename__= 'big_daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable31(G_Base):
    __tablename__= 'buy_big_daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable31(G_Base):
    __tablename__= 'sell_big_daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable32(G_Base):
    __tablename__= 'big_daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable32(G_Base):
    __tablename__= 'buy_big_daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable32(G_Base):
    __tablename__= 'sell_big_daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable33(G_Base):
    __tablename__= 'big_daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable33(G_Base):
    __tablename__= 'buy_big_daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable33(G_Base):
    __tablename__= 'sell_big_daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable34(G_Base):
    __tablename__= 'big_daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable34(G_Base):
    __tablename__= 'buy_big_daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable34(G_Base):
    __tablename__= 'sell_big_daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable35(G_Base):
    __tablename__= 'big_daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable35(G_Base):
    __tablename__= 'buy_big_daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable35(G_Base):
    __tablename__= 'sell_big_daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable36(G_Base):
    __tablename__= 'big_daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable36(G_Base):
    __tablename__= 'buy_big_daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable36(G_Base):
    __tablename__= 'sell_big_daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable37(G_Base):
    __tablename__= 'big_daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable37(G_Base):
    __tablename__= 'buy_big_daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable37(G_Base):
    __tablename__= 'sell_big_daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable38(G_Base):
    __tablename__= 'big_daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable38(G_Base):
    __tablename__= 'buy_big_daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable38(G_Base):
    __tablename__= 'sell_big_daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable39(G_Base):
    __tablename__= 'big_daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable39(G_Base):
    __tablename__= 'buy_big_daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable39(G_Base):
    __tablename__= 'sell_big_daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable40(G_Base):
    __tablename__= 'big_daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable40(G_Base):
    __tablename__= 'buy_big_daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable40(G_Base):
    __tablename__= 'sell_big_daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable41(G_Base):
    __tablename__= 'big_daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable41(G_Base):
    __tablename__= 'buy_big_daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable41(G_Base):
    __tablename__= 'sell_big_daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable42(G_Base):
    __tablename__= 'big_daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable42(G_Base):
    __tablename__= 'buy_big_daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable42(G_Base):
    __tablename__= 'sell_big_daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable43(G_Base):
    __tablename__= 'big_daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable43(G_Base):
    __tablename__= 'buy_big_daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable43(G_Base):
    __tablename__= 'sell_big_daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable44(G_Base):
    __tablename__= 'big_daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable44(G_Base):
    __tablename__= 'buy_big_daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable44(G_Base):
    __tablename__= 'sell_big_daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable45(G_Base):
    __tablename__= 'big_daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable45(G_Base):
    __tablename__= 'buy_big_daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable45(G_Base):
    __tablename__= 'sell_big_daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable46(G_Base):
    __tablename__= 'big_daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable46(G_Base):
    __tablename__= 'buy_big_daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable46(G_Base):
    __tablename__= 'sell_big_daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable47(G_Base):
    __tablename__= 'big_daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable47(G_Base):
    __tablename__= 'buy_big_daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable47(G_Base):
    __tablename__= 'sell_big_daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable48(G_Base):
    __tablename__= 'big_daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable48(G_Base):
    __tablename__= 'buy_big_daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable48(G_Base):
    __tablename__= 'sell_big_daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BigDailyPriceTable49(G_Base):
    __tablename__= 'big_daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyBigDailyPriceTable49(G_Base):
    __tablename__= 'buy_big_daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellBigDailyPriceTable49(G_Base):
    __tablename__= 'sell_big_daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
