

id_file = open('StockList.txt','r')

o_file = open('schema.txt','w+')

schema = '''
class stock__STOCK_ID__(__Base):
    __tablename__= '__STOCK_ID__'
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
    
Index('__STOCK_ID___index',stock__STOCK_ID__.bigvolumn_status,stock__STOCK_ID__.trade_date,stock__STOCK_ID__.trade_time)
    '''


#line = id_file.readline()

for line in id_file.readlines():
    line = line.strip('\n')
    new_schema = schema.replace('__STOCK_ID__', line)
    o_file.write(new_schema)

id_file.close()
o_file.close()
    
    