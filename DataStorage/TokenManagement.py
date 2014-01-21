from DBModule.Modules import G_DB
from DBModule.Modules import *
from sqlalchemy.sql import or_
from datetime import timedelta

class TokenManagement():
    __DB = None
    
    def __init__(self):
        self.db_con = G_DB
        
    def get_initial_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(or_(StockManagement.status==0, StockManagement.status == None)).limit(20).all()
        session.close()
        stockids = []
        for stock in stocks:
            stockids.append(stock.market + stock.id)
        return stockids
    
    def get_all_error_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(StockManagement.status==3).all()
        session.close()
        stockids = []
        for stock in stocks:
            stockids.append(stock.market + stock.id)
        return stockids
    
    def get_error_token(self):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement).filter(StockManagement.status==3).limit(20).all()
        session.close()
        return stocks
    
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