from Crawler.StockListCrawler import StockListCrawler
from mimify import File
from test.test_decimal import file
from DBModule.Modules import *
import urllib

crawler = StockListCrawler()

crawler.crawl()

_file = open('test.txt','w')

DB = DB_Base('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
Base = DB.get_base()

session = DB.get_session()




#stockmanagement = StockManagement()
#print crawler.get_stock_dict()
stocks = []

a = crawler.get_stock_dict().items()[0][1]

#b = a.encode('hex')

#_file.write(a)

stock_dict = crawler.get_stock_dict();

<<<<<<< HEAD:src/crawl_test.py
#db_stocks = session.query(StockManagement).filter(StockManagement.id in stock_dict.keys()).all();

=======
>>>>>>> ec6bf42550f8595a9e8f61c26dcc7b6eff52fa15:src/stock_list_crawl.py
for key in stock_dict:
    #value = value.decode('utf-8').encode('gb2312')
    #retStr = value.decode('hex')
    '''key += ":"
    key += value
    key += "\n"
    _file.write(key)'''
    SM = StockManagement()
    SM.id = key[2:]
    SM.market = key[0:2]
    SM.name = stock_dict[key]
    SM1 = session.merge(SM)
    #if SM1.data_end_date:
    #   print SM1
    #print SM1

session.commit()


_file.close()
