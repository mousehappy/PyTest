#coding=utf-8
from DBModule.Modules import *
from datetime import date
from sqlalchemy.sql import or_
from datetime import timedelta
from CrawlConfig import G_Config
from exceptions import Exception
import os

class ProcessManager():
    __DB = None
    __data_dir = None
    
    def __init__(self, DBCon = None):
        if DBCon:
            self.__DB = DB_Base(DBCon)
        else:
            self.__DB = G_DB
        
        self.__data_dir = G_Config.data_dir
            
    def GetProcessStocks(self):
        session = self.__DB.get_session()
        
        NowDate = date.today()
        NowDateStr = NowDate.isoformat()
        
        stocks = session.query(StockManagement, StockBaseInfo).filter(StockManagement.id == StockBaseInfo.id, StockManagement.status == 2)\
        .filter(or_(StockManagement.processed_date == None, StockManagement.processed_date < StockManagement.data_end_date)).all()
        
        #session.commit()
        session.expunge_all()
        session.close()
        return stocks
    
    def ProcessData(self):
        stocks = self.GetProcessStocks()
        for stock in stocks:
            SM = stock[0]
            SBI = stock[1]
            ATradeShare = SBI.tradable_share
            startdate = SM.data_begin_date
            enddate = SM.data_end_date
            if SM.processed_date != None:
                startdate = SM.processed_date + timedelta(1)
            DateDiff = enddate - startdate
            for i in xrange(0, DateDiff.days):
            #for i in xrange(0, 10):
                DataDate = startdate + timedelta(i)
                self.ProcessStock(SM.id, DataDate, ATradeShare)
        
    
    def ProcessStock(self, stockid, datadate, ATradeShare):
        StockPath = self.__data_dir
        os.chdir(StockPath)
        if not os.path.isdir(stockid):
            raise Exception(stockid + " data not found")
            return
        os.chdir(stockid)
        fname = datadate.isoformat() + ".txt"
        if not os.path.isfile(fname):
            return
        sfile = open(fname)
        trades = sfile.readlines()
        sfile.close()
        #begin session
        session = self.__DB.get_session()
        #initialize coresponding module name
        m_name = 'stocktbl'+stockid[-1]+'()'
        init_price = 0
        end_price = 0
        high_price = 0
        low_price = 0
        for i in xrange(1, len(trades)):
            line = trades[i].strip('\n')
            fields = line.split('\t')
            t_time = fields[0]
            t_price = float(fields[1])
            if fields[2] == '--':
                fields[2] = 0
            t_diff = float(fields[2])
            t_count = int(fields[3])
            t_amout = int(fields[4])
            t_style = fields[5]
            
            if i == 1:
                end_price = t_price
                high_price = t_price
                low_price = t_price
            else:
                if high_price < t_price:
                    high_price = t_price
                if low_price > t_price:
                    low_price = t_price
            if i == len(trades)-1:
                init_price = t_price
            
            if t_style == u'买盘':
                t_style = 1
            elif t_style == u'卖盘':
                t_style = 2
            else:
                t_style = 3
                
            #big deal by count
            BigType = 0
            if t_amout > 30000000:
                BigType = 500
            elif t_amout > 20000000:
                BigType = 400
            elif t_amout > 10000000:
                BigType = 300
            elif t_amout > 5000000:
                BigType = 250
            elif t_amout > 2000000:
                BigType = 220
            elif t_amout > 1000000:
                BigType = 210
            elif t_amout > 500000:
                BigType = 205
            elif t_amout > 200000:
                BigType = 202
            elif t_amout > 100000:
                BigType = 201
            
            if BigType != 0:
                BigAmount = eval(m_name)
                BigAmount.stock_id = int(stockid[2:])
                BigAmount.bigvolumn_status = BigType
                BigAmount.trade_time = t_time
                BigAmount.trade_date = datadate
                BigAmount.price = t_price
                BigAmount.variation = t_diff
                BigAmount.trade_volumn = t_count
                BigAmount.trade_value = t_amout
                BigAmount.trade_status = t_style
                session.merge(BigAmount)
            
        #calculate price variation
        
            
        session.commit()
        session.close()
            #big deal by amount
            




















