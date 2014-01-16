import os
from DBModule.Modules import *
from sqlalchemy import or_
from sqlalchemy.sql.operators import like_op
from CrawlManager import CrawlManager
from datetime import *
import time
from MySQLdb.constants.FIELD_TYPE import NULL

class CrawlServer(object):
    __DB = None
    __CrawlManager = None
    __Crawl_Finish = False
    
    def __init__(self, db_con = None):
        object.__init__(self)
        self.__CrawlManager = CrawlManager()
        if db_con != None:
            self.__DB = DB_Base(db_con)
        
    def set_database(self, db_con):
        self.__DB = DB_Base(db_con)
        
    def check_date(self,date):
        now = datetime.now()
        if now.hour > 20:
                pass
        else:
            date = date - timedelta(1)
        return date
    
    
    def inital_crawl(self, days = 360, *stockids):
        #print "argu length: %d"%len(stockids)
        end_date = date.today()
        end_date = self.check_date(end_date)
        start_date = end_date - timedelta(days)
        stocks = self.get_initial_token()
        stock_count = len(stocks)
        while stock_count != 0:
            task_dict = {}
            for stock in stocks:
                task_dict.setdefault(stock, []).append(start_date)
                task_dict[stock].append(end_date)
            
            self.__CrawlManager.generate_tasks(tasks = task_dict)
            self.__CrawlManager.start_crawl()
            self.__Crawl_Finish = False
            self.waiting_for_crawl()
            error_records = self.__CrawlManager.get_errors()
            self.complete_crawl(task_dict, error_records)
            stocks = self.get_initial_token()
            stock_count = len(stocks)
        
        error_sms = self.get_error_token()
        stock_count = len(error_sms)
        while stock_count != 0:
            task_dick = {}
            for stock in error_sms:
                stockid = stock.id
                task_dict.setdefault(stockid, []).append(stock.data_begin_date)
                task_dict[stockid].append(end_date)
            self.__CrawlManager.generate_tasks(tasks = task_dict)
            self.__CrawlManager.start_crawl()
            self.__Crawl_Finish = False
            self.waiting_for_crawl()
            error_records = self.__CrawlManager.get_errors()
            self.complete_crawl(task_dict, error_records)
            error_sms = self.get_error_token()
            stock_count = len(error_sms)
        
        print "Initial crawl finished!!"
                #task_dict.setdefault(stock.id, []).append()
                
    def test_error_crawl(self):
        end_date = date.today()
        end_date = self.check_date(end_date)
        error_sms = self.get_error_token()
        stock_count = len(error_sms)
        while stock_count != 0:
            task_dick = {}
            for stock in error_sms:
                stockid = stock.id
                stock_begin_date = stock.data_begin_date
                stock_end_date = stock.data_end_date
                year = stock_begin_date[:4]
                month = stock_begin_date[5:6]
                day = stock_begin_date[7:8]
                error_begin_date = date(year, month, day)
                task_dick.setdefault(stockid, []).append(error_begin_date)
                task_dick[stockid].append(end_date)
    
    def error_recrawl(self, days = 360, *stockids):
        #print "argu length: %d"%len(stockids)
        end_date = date.today()
        end_date = self.check_date(end_date)
        start_date = end_date - timedelta(days)
        stocks = self.get_error_token()
        stock_count = len(stocks)
        while stock_count != 0:
            task_dict = {}
            for stock in stocks:
                task_dict.setdefault(stock, []).append(start_date)
                task_dict[stock].append(end_date)
            
            self.__CrawlManager.generate_tasks(tasks = task_dict)
            self.__CrawlManager.start_crawl()
            self.__Crawl_Finish = False
            self.waiting_for_crawl()
            error_records = self.__CrawlManager.get_errors()
            self.complete_crawl(task_dict, error_records)
            stocks = self.get_initial_token()
            stock_count = len(stocks)
            
    def get_initial_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(or_(StockManagement.status==0, StockManagement.status == None)).limit(20).all()
        session.close()
        stockids = []
        for stock in stocks:
            stockids.append(stock.id)
        return stockids
            
    def get_all_error_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(StockManagement.status==3).all()
        session.close()
        stockids = []
        for stock in stocks:
            stockids.append(stock.id)
        return stockids
    
    def get_error_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(StockManagement.status==3).limit(20).all()
        session.close()
        return stocks
    
    def waiting_for_crawl(self):
        while True:
            crawler_count = self.__CrawlManager.get_alive_crwaler()
            if  crawler_count != 0:
                time.sleep(5)
            else:
                print "Crawl finished!!"
                break
    
    def print_tasks(self): 
        queue = self.__CrawlManager.get_task_queue()
        print "task queue size is ",queue.qsize()
        while True:
            try:
                task = queue.get_nowait()
                print task
            except:
                break
    
    def complete_crawl(self, task_dict, error_records):
        session = self.__DB.get_session()
        crawled_stocks = session.query(StockManagement).filter(StockManagement.id in task_dict.keys()).all()
        for stockid in task_dict:
            SM = StockManagement()
            SM.id = stockid
            SM.data_begin_date = task_dict[stockid][0]
            SM.data_end_date = task_dict[stockid][1]
            SM.status = 2
            SM = session.merge(SM)
        
        for stockid in error_records:
            SM = StockManagement()
            SM.id = stockid
            SM.status = 3
            SM.data_end_date = error_records[stockid]- timedelta(1)
            SM = session.merge(SM)

        session.commit()
        session.close()
        self.__CrawlManager.clear()
            