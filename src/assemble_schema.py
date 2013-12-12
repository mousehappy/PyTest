

id_file = open('StockList.txt','r')

o_file = open('schema.txt','w+')

schema = '''class stock__STOCK_ID__(__Base):
    __tablename__= '__STOCK_ID__'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    status = Column(Integer, default = 0)
    data_begin_date = Column(Date, nullable = True)
    data_end_date = Column(Date, nullable = True)
    insert_timestamp = Column(DateTime, default = func.current_timestamp())
    update_timestamp = Column(DateTime, nullable = True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return "<Stock(id='%s', name='%s',status='%s','last_crawl_date'='%s')>" % (self.id, self.name, self.status, self.date_end_date)'''

line = id_file.readline()

line = line.strip('\n')

new_schema = schema.replace('__STOCK_ID__', line)

print line

print new_schema

id_file.close()
o_file.close()
    
    