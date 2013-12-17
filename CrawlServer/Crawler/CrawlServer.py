import os
from DBModule.Modules import *
from sqlalchemy import or_
from sqlalchemy.sql.operators import like_op
from CrawlManager import CrawlManager
from datetime import *
import time

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
        if len(stockids) > 0:
            for sid in stockids:
                print sid
                pass
        else:
            session = self.__DB.get_session()
            stocks = session.query(StockManagement.id).filter(StockManagement.status==0).limit(100).all()
            session.close()
            
            end_date = date.today()
            end_date = self.check_date(end_date)
            start_date = end_date - timedelta(days)
            task_dict = {}
            for stock in stocks:
                stockid = stock[0].encode('utf-8')
                task_dict.setdefault(stockid, []).append(start_date)
                task_dict[stockid].append(end_date)
            
            self.__CrawlManager.generate_tasks(tasks = task_dict)
            self.__CrawlManager.start_crawl()
            self.__Crawl_Finish = False
    
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
        

            