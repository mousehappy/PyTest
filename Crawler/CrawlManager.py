from datetime import date
import datetime
import time
import Queue
from datetime import timedelta
from StockCrawler import StockCrawler
import threading
from StockDataCrawler import StockDataCrawler
import os

class CrawlManager:
    __start_date = date(2000,01,01)
    __end_date = date(2000,01,01)
    __task_queue = Queue.Queue()
    __thread_count = 5
    __thread_pool = []
    __data_dir = r"C:\StockData"
    __error_dict = {}
    
    def __init__(self):
        pass
    
    def set_crawl_scope(self, start_date, end_date = date.today().isoformat()):
        start_tuple = start_date.split("-")
        end_tuple = end_date.split("-")
        self.__start_date = date(int(start_tuple[0]),int(start_tuple[1]),int(start_tuple[2]))
        self.__end_date = date(int(end_tuple[0]),int(end_tuple[1]),int(end_tuple[2]))
        
    def generate_tasks(self, stockid = None, tasks = None):
        if stockid != None:
            os.chdir(self.__data_dir)
            if not os.path.isdir(stockid):
                os.mkdir(stockid)
            n = self.__end_date - self.__start_date
            for i in xrange(0,n.days):
                crawldate = self.__start_date+timedelta(i)
                self.__task_queue.put((stockid,crawldate.isoformat()))
        
        if tasks != None:
            if not isinstance(tasks, dict):
                print "Task input with wront struct! The format should be {stockid:[start_date,end_date],...}"
                return
            for item in tasks.iteritems():
                stockid = item[0]
                os.chdir(self.__data_dir)
                if not os.path.isdir(stockid):
                    os.mkdir(stockid)
                start_date = item[1][0]
                end_date = item[1][1]
                interval = end_date - start_date
                for i in range(interval.days+1):
                    crawl_date = start_date + timedelta(i)
                    self.__task_queue.put((stockid, crawl_date))
    
 
    def start_crawl(self):
        for i in range(self.__thread_count):
            self.__thread_pool.append(StockDataCrawler(self.__task_queue, self.__error_dict))
        
        for t in self.__thread_pool:
            t.start()
    
    def stop_crawl(self):
        for t in self.__thread_pool:
            t.stop()
            t.join()
            
    def get_alive_crwaler(self):
        t_count = 0
        for t in self.__thread_pool:
            if t.isAlive():
                t_count += 1
        return t_count
    
    def get_task_queue(self):
        return self.__task_queue
    
    def get_errors(self):
        return self.__error_dict
                