from CrawlServer.Crawler.StockListCrawler import StockListCrawler
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

for key,value in crawler.get_stock_dict().items():
    #value = value.decode('utf-8').encode('gb2312')
    #retStr = value.decode('hex')
    '''key += ":"
    key += value
    key += "\n"
    _file.write(key)'''
    stocks.append({'id':key,'name':value})

session.execute(StockManagement.__table__.insert(), stocks)

session.commit()

_file.close()
