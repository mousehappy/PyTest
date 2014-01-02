from Modules import *


class StockManager():
    __DB = None
    def __init__(self):
        global G_DB
        if self.__DB == None:
            self.__DB = G_DB
    
    def SelectInitialStock(self,limit=100):
        session = self.__DB.get_session()
        stocks = session.query(StockManagement.id).filter(StockManagement.status==0).limit(100).all()
        session.close()
        return stocks
    
    def SetInitialCrawl(self,*stocks):
        for stock in stocks:
            pass