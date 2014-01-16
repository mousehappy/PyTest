import threading
import time
import Queue
import sys
import pycurl
import cStringIO
import os

class StockDataCrawler(threading.Thread):
    'http://market.finance.sina.com.cn/downxls.php?date=2013-12-05&symbol=sz300027'
    __data_dir = r"C:\StockData"
    __url = r"http://market.finance.sina.com.cn/downxls.php?"
    __stop = False
    __task_lock = None
    __task_count = None
    __error_dict = None
    
    def __init__(self, task_queue, error_dict):
        threading.Thread.__init__(self)
        self.queue = task_queue
        if StockDataCrawler.__task_lock == None:
            StockDataCrawler.__task_lock = threading.Lock()
        if StockDataCrawler.__task_count == None:
            StockDataCrawler.__task_count = task_queue.qsize()
        if StockDataCrawler.__error_dict == None:
            StockDataCrawler.__error_dict = error_dict
        
    def stop(self):
        self.__stop = True
    
    def get_next_task(self):
        task = None
        StockDataCrawler.__task_lock.acquire()
        while True:
            try:
                task = self.queue.get(True, 1)
            except Queue.Empty:
                print "Thread %s is finished!" % self.name
                break
            else:
                if task[0] in StockDataCrawler.__error_dict.keys():
                    continue
                else:
                    break 
        StockDataCrawler.__task_lock.release()
        time.sleep(1)
        return task
    
    def run(self):
        while True:
            if self.__stop:
                return
            buf = cStringIO.StringIO()
            task = self.get_next_task()
            if task == None:
                return
            
            stockid = task[0]
            crawldate = task[1]
            crawldate_str = crawldate.isoformat()
            
            curl = pycurl.Curl()
            url = self.__url + "date=" + crawldate_str + "&" + "symbol=" + stockid
            curl.setopt(pycurl.URL, url)
            curl.setopt(pycurl.FOLLOWLOCATION, 1)
            curl.setopt(pycurl.MAXREDIRS, 5)
            curl.setopt(pycurl.CONNECTTIMEOUT, 30)
            curl.setopt(pycurl.TIMEOUT, 300)
            curl.setopt(pycurl.NOSIGNAL, 1)
            curl.setopt(pycurl.WRITEFUNCTION, buf.write)
            for try_i in range(1, 4):
                try:
                    curl.perform()
                except:
                    print "exception occured in crawl"
                    import traceback
                    traceback.print_exc(file=sys.stderr)
                    sys.stderr.flush()
                    if try_i == 3:
                        self.record_error(self, stockid, crawldate)
                else:
                    content = buf.getvalue().decode('gb2312')
                    if len(content) == 0:
                        self.record_error(stockid, crawldate)
                    elif len(content) > 1000:
                        file_name = self.__data_dir + "\\" + stockid[2:] + "\\" + crawldate_str + ".txt"
                        file = open(file_name, 'w+')
                        file.write(content)
                        file.close()
                    break
            else:
                self.queue.put((stockid, crawldate))
            buf.close()
            curl.close()
            print "Crawl stock %s of %s finished!" % (stockid, crawldate)
    
    
    def record_error(self, stockid, crawldate):
        StockDataCrawler.__task_lock.acquire()
        if stockid in StockDataCrawler.__error_dict.keys():
            StockDataCrawler.__error_dict[stockid] = (StockDataCrawler.__error_dict[stockid] < crawldate and StockDataCrawler.__error_dict[stockid]) or crawldate
        else:
            StockDataCrawler.__error_dict[stockid] = crawldate
        StockDataCrawler.__task_lock.release()
    
        
        
        
                
