from sqlalchemy import Column, Integer, Sequence, String, Time, Date, DateTime, Numeric
from sqlalchemy.sql.expression import func
from Modules import G_Base

class DailyPriceTable0(G_Base):
    __tablename__= 'daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable0(G_Base):
    __tablename__= 'sell_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable0(G_Base):
    __tablename__= 'buy_daily_price_table0'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable1(G_Base):
    __tablename__= 'daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable1(G_Base):
    __tablename__= 'sell_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable1(G_Base):
    __tablename__= 'buy_daily_price_table1'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable2(G_Base):
    __tablename__= 'daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable2(G_Base):
    __tablename__= 'sell_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable2(G_Base):
    __tablename__= 'buy_daily_price_table2'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable3(G_Base):
    __tablename__= 'daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable3(G_Base):
    __tablename__= 'sell_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable3(G_Base):
    __tablename__= 'buy_daily_price_table3'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable4(G_Base):
    __tablename__= 'daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable4(G_Base):
    __tablename__= 'sell_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable4(G_Base):
    __tablename__= 'buy_daily_price_table4'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable5(G_Base):
    __tablename__= 'daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable5(G_Base):
    __tablename__= 'sell_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable5(G_Base):
    __tablename__= 'buy_daily_price_table5'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable6(G_Base):
    __tablename__= 'daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable6(G_Base):
    __tablename__= 'sell_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable6(G_Base):
    __tablename__= 'buy_daily_price_table6'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable7(G_Base):
    __tablename__= 'daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable7(G_Base):
    __tablename__= 'sell_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable7(G_Base):
    __tablename__= 'buy_daily_price_table7'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable8(G_Base):
    __tablename__= 'daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable8(G_Base):
    __tablename__= 'sell_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable8(G_Base):
    __tablename__= 'buy_daily_price_table8'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable9(G_Base):
    __tablename__= 'daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable9(G_Base):
    __tablename__= 'sell_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable9(G_Base):
    __tablename__= 'buy_daily_price_table9'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable10(G_Base):
    __tablename__= 'daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable10(G_Base):
    __tablename__= 'sell_daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable10(G_Base):
    __tablename__= 'buy_daily_price_table10'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable11(G_Base):
    __tablename__= 'daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable11(G_Base):
    __tablename__= 'sell_daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable11(G_Base):
    __tablename__= 'buy_daily_price_table11'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable12(G_Base):
    __tablename__= 'daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable12(G_Base):
    __tablename__= 'sell_daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable12(G_Base):
    __tablename__= 'buy_daily_price_table12'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable13(G_Base):
    __tablename__= 'daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable13(G_Base):
    __tablename__= 'sell_daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable13(G_Base):
    __tablename__= 'buy_daily_price_table13'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable14(G_Base):
    __tablename__= 'daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable14(G_Base):
    __tablename__= 'sell_daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable14(G_Base):
    __tablename__= 'buy_daily_price_table14'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable15(G_Base):
    __tablename__= 'daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable15(G_Base):
    __tablename__= 'sell_daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable15(G_Base):
    __tablename__= 'buy_daily_price_table15'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable16(G_Base):
    __tablename__= 'daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable16(G_Base):
    __tablename__= 'sell_daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable16(G_Base):
    __tablename__= 'buy_daily_price_table16'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable17(G_Base):
    __tablename__= 'daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable17(G_Base):
    __tablename__= 'sell_daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable17(G_Base):
    __tablename__= 'buy_daily_price_table17'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable18(G_Base):
    __tablename__= 'daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable18(G_Base):
    __tablename__= 'sell_daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable18(G_Base):
    __tablename__= 'buy_daily_price_table18'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable19(G_Base):
    __tablename__= 'daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable19(G_Base):
    __tablename__= 'sell_daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable19(G_Base):
    __tablename__= 'buy_daily_price_table19'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable20(G_Base):
    __tablename__= 'daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable20(G_Base):
    __tablename__= 'sell_daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable20(G_Base):
    __tablename__= 'buy_daily_price_table20'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable21(G_Base):
    __tablename__= 'daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable21(G_Base):
    __tablename__= 'sell_daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable21(G_Base):
    __tablename__= 'buy_daily_price_table21'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable22(G_Base):
    __tablename__= 'daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable22(G_Base):
    __tablename__= 'sell_daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable22(G_Base):
    __tablename__= 'buy_daily_price_table22'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable23(G_Base):
    __tablename__= 'daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable23(G_Base):
    __tablename__= 'sell_daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable23(G_Base):
    __tablename__= 'buy_daily_price_table23'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable24(G_Base):
    __tablename__= 'daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable24(G_Base):
    __tablename__= 'sell_daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable24(G_Base):
    __tablename__= 'buy_daily_price_table24'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable25(G_Base):
    __tablename__= 'daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable25(G_Base):
    __tablename__= 'sell_daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable25(G_Base):
    __tablename__= 'buy_daily_price_table25'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable26(G_Base):
    __tablename__= 'daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable26(G_Base):
    __tablename__= 'sell_daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable26(G_Base):
    __tablename__= 'buy_daily_price_table26'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable27(G_Base):
    __tablename__= 'daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable27(G_Base):
    __tablename__= 'sell_daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable27(G_Base):
    __tablename__= 'buy_daily_price_table27'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable28(G_Base):
    __tablename__= 'daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable28(G_Base):
    __tablename__= 'sell_daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable28(G_Base):
    __tablename__= 'buy_daily_price_table28'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable29(G_Base):
    __tablename__= 'daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable29(G_Base):
    __tablename__= 'sell_daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable29(G_Base):
    __tablename__= 'buy_daily_price_table29'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable30(G_Base):
    __tablename__= 'daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable30(G_Base):
    __tablename__= 'sell_daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable30(G_Base):
    __tablename__= 'buy_daily_price_table30'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable31(G_Base):
    __tablename__= 'daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable31(G_Base):
    __tablename__= 'sell_daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable31(G_Base):
    __tablename__= 'buy_daily_price_table31'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable32(G_Base):
    __tablename__= 'daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable32(G_Base):
    __tablename__= 'sell_daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable32(G_Base):
    __tablename__= 'buy_daily_price_table32'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable33(G_Base):
    __tablename__= 'daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable33(G_Base):
    __tablename__= 'sell_daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable33(G_Base):
    __tablename__= 'buy_daily_price_table33'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable34(G_Base):
    __tablename__= 'daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable34(G_Base):
    __tablename__= 'sell_daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable34(G_Base):
    __tablename__= 'buy_daily_price_table34'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable35(G_Base):
    __tablename__= 'daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable35(G_Base):
    __tablename__= 'sell_daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable35(G_Base):
    __tablename__= 'buy_daily_price_table35'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable36(G_Base):
    __tablename__= 'daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable36(G_Base):
    __tablename__= 'sell_daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable36(G_Base):
    __tablename__= 'buy_daily_price_table36'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable37(G_Base):
    __tablename__= 'daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable37(G_Base):
    __tablename__= 'sell_daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable37(G_Base):
    __tablename__= 'buy_daily_price_table37'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable38(G_Base):
    __tablename__= 'daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable38(G_Base):
    __tablename__= 'sell_daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable38(G_Base):
    __tablename__= 'buy_daily_price_table38'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable39(G_Base):
    __tablename__= 'daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable39(G_Base):
    __tablename__= 'sell_daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable39(G_Base):
    __tablename__= 'buy_daily_price_table39'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable40(G_Base):
    __tablename__= 'daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable40(G_Base):
    __tablename__= 'sell_daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable40(G_Base):
    __tablename__= 'buy_daily_price_table40'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable41(G_Base):
    __tablename__= 'daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable41(G_Base):
    __tablename__= 'sell_daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable41(G_Base):
    __tablename__= 'buy_daily_price_table41'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable42(G_Base):
    __tablename__= 'daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable42(G_Base):
    __tablename__= 'sell_daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable42(G_Base):
    __tablename__= 'buy_daily_price_table42'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable43(G_Base):
    __tablename__= 'daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable43(G_Base):
    __tablename__= 'sell_daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable43(G_Base):
    __tablename__= 'buy_daily_price_table43'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable44(G_Base):
    __tablename__= 'daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable44(G_Base):
    __tablename__= 'sell_daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable44(G_Base):
    __tablename__= 'buy_daily_price_table44'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable45(G_Base):
    __tablename__= 'daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable45(G_Base):
    __tablename__= 'sell_daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable45(G_Base):
    __tablename__= 'buy_daily_price_table45'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable46(G_Base):
    __tablename__= 'daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable46(G_Base):
    __tablename__= 'sell_daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable46(G_Base):
    __tablename__= 'buy_daily_price_table46'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable47(G_Base):
    __tablename__= 'daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable47(G_Base):
    __tablename__= 'sell_daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable47(G_Base):
    __tablename__= 'buy_daily_price_table47'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable48(G_Base):
    __tablename__= 'daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable48(G_Base):
    __tablename__= 'sell_daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable48(G_Base):
    __tablename__= 'buy_daily_price_table48'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class DailyPriceTable49(G_Base):
    __tablename__= 'daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class SellDailyPriceTable49(G_Base):
    __tablename__= 'sell_daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())

class BuyDailyPriceTable49(G_Base):
    __tablename__= 'buy_daily_price_table49'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
