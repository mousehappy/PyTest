
tbl_str = '''class stocktblNOO(G_Base):
    __tablename__= 'stocktblNOO'
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
    
Index('stocktblNOO_index',stocktblNOO.stock_id,stocktblNOO.bigvolumn_status,stocktblNOO.trade_date,stocktblNOO.trade_time)'''

price_tbl = '''class DailyPriceTableNOO(G_Base):
    __tablename__= 'daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''

bprice_tbl = '''class SellDailyPriceTableNOO(G_Base):
    __tablename__= 'sell_daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''
    
sprice_tbl = '''class BuyDailyPriceTableNOO(G_Base):
    __tablename__= 'buy_daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''

big_tbl = '''class BigDailyPriceTableNOO(G_Base):
    __tablename__= 'big_daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''
    
buy_big_tbl = '''class BuyBigDailyPriceTableNOO(G_Base):
    __tablename__= 'buy_big_daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''

sell_big_tbl = '''class SellBigDailyPriceTableNOO(G_Base):
    __tablename__= 'sell_big_daily_price_tableNOO'
    stock_id = Column(String(8),primary_key=True)
    trade_date = Column(Date,primary_key=True)
    price = Column(Numeric(10,2),primary_key=True)
    big_type = Column(Integer, primary_key=True, autoincrement=False)
    count = Column(Integer)
    amount = Column(Integer)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())'''
    
f_out = open('tbl_const','w+')
f_price = open('tbl_price','w+')
f_big = open('tbl_big','w+')

for i in xrange(0,100):
    const_str = tbl_str.replace('NOO', str(i))
    f_out.write(const_str)
    f_out.write('\n\n')
    
    const_str = price_tbl.replace('NOO', str(i))
    f_price.write(const_str)
    f_price.write('\n\n')
    
    const_str = bprice_tbl.replace('NOO', str(i))
    f_price.write(const_str)
    f_price.write('\n\n')
    
    const_str = sprice_tbl.replace('NOO', str(i))
    f_price.write(const_str)
    f_price.write('\n\n')
    
    const_str = big_tbl.replace('NOO', str(i))
    f_big.write(const_str)
    f_big.write('\n\n')
    
    const_str = buy_big_tbl.replace('NOO', str(i))
    f_big.write(const_str)
    f_big.write('\n\n')
    
    const_str = sell_big_tbl.replace('NOO', str(i))
    f_big.write(const_str)
    f_big.write('\n\n')
    
    
f_out.close()
f_price.close()
f_big.close()
    
