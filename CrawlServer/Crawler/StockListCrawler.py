from datetime import date
from ..Parser import StockListParser

import sys
import pycurl
import cStringIO


filename = 'stocklist.html'
#url = 'http://www.163.com'

class StockListCrawler:
    def __init__(self, url='http://quote.eastmoney.com/stocklist.html'):
        self.update_date = date.today()
        self.parser = StockListParser.StockListParser()
        self.stock_list = []
        self.stock_name_list = []
        self.stock_dict = {}
        self.url = url
    
    def crawl(self):
        buf = cStringIO.StringIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, self.url)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.MAXREDIRS, 5)
        curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.NOSIGNAL, 1)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        try_time = 0
        while try_time < 3:
            try:
                curl.perform()
            except pycurl.error:
                try_time+=1
                print 'One error happened with stock list crawl with error', pycurl.error
                continue
            else:
                context=buf.getvalue()
                self.parser.feed(context)
                self.stock_list = self.parser.get_stock_list()
                self.stock_name_list = self.parser.get_stock_names()
                self.stock_dict = self.parser.get_stock_dict()
                sys.stdout.write("Stock list crwal finish")
                sys.stdout.flush()
                break
        if try_time >= 3:
            sys.stdout.write("Stock list crwal fail")
            sys.stdout.flush()
        
        curl.close()
        buf.close()
                    
    def get_stock_list(self):
        return self.stock_list
    
    def get_stock_dict(self):
        return self.stock_dict
    
    def refresh_DB(self):
        if len(self.stocklist) == 0:
            return
        
        
