#coding=utf-8
from DBModule.Modules import *
from datetime import date
from sqlalchemy.sql import or_
from datetime import timedelta
from CrawlConfig import G_Config
from exceptions import Exception
from DBModule.DailyPriceTable import *
from DBModule.BigDailyPriceTable import *
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
        .filter(or_(StockManagement.processed_date == None, StockManagement.processed_date < StockManagement.data_end_date)).limit(5).all()
        
        for stock in stocks:
            #SM = StockManagement()
            #SM.id = stock[0].id
            stock[0].status = 5
        
        session.commit()
        session.expunge_all() 
        session.close()
        return stocks
    
    def ProcessData(self):
        stocks = self.GetProcessStocks()
        while len(stocks) > 0:
            print 'Start processing stock data:',[stock[0].id for stock in stocks]
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
                self.FinishProcessStock(SM.id, enddate)
            print 'Finish processing stock data:',[stock[0].id for stock in stocks]
            stocks = self.GetProcessStocks()
    
    def FinishProcessStock(self, stockid, enddate):
        session = self.__DB.get_session()
        SM = StockManagement()
        SM.id = stockid
        SM.status = 2
        SM.processed_date = enddate
        session.close() 
    
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
        
        #daily record variables
        init_price = 0
        end_price = 0
        high_price = 0
        low_price = 0
        trade_amount = 0
        trade_count = 0
        sell_amount = 0
        sell_count = 0
        buy_amount = 0
        buy_count = 0
        neutral_amount = 0
        neutral_count = 0
        variation = 0
        variat_rate = 0
        amplitude = 0
        exchange_rate = 0
        buy_rate = 0
        sell_rate = 0
        neutral_rate = 0
        
        #price table
        PriceDictCount = {}
        SellPriceDictCount = {}
        BuyPriceDictCount = {}
        PriceDictAmount = {}
        SellPriceDictAmount = {}
        BuyPriceDictAmount = {}
        
        BigPriceDictCount = {}
        BigSellPriceDictCount = {}
        BigBuyPriceDictCount = {}
        BigPriceDictAmount = {}
        BigSellPriceDictAmount = {}
        BigBuyPriceDictAmount = {}
        BigTypes = [201, 202, 205, 210, 220, 250, 300, 400, 500]
        for t in BigTypes:
            BigPriceDictCount[t] = {}
            BigSellPriceDictCount[t] = {}
            BigBuyPriceDictCount[t] = {}
            BigPriceDictAmount[t] = {}
            BigSellPriceDictAmount[t] = {}
            BigBuyPriceDictAmount[t] = {}
         
        
        for i in xrange(1, len(trades)):
            line = trades[i].strip('\n')
            fields = line.split('\t')
            t_time = fields[0]
            t_price = float(fields[1])
            if fields[2] == '--':
                fields[2] = 0
            t_diff = float(fields[2])
            t_count = int(fields[3])
            t_amount = int(fields[4])
            t_style = fields[5]
            
            #get sum
            trade_amount += t_amount
            trade_count += t_count
            
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
                buy_amount += t_amount
                buy_count += t_count
            elif t_style == u'卖盘':
                t_style = 2
                sell_amount += t_amount
                sell_count += t_count
            else:
                t_style = 3
                neutral_amount += t_amount
                neutral_count += t_count
                
            #big deal by count
            BigType = 0
            if t_amount > 30000000:
                BigType = 500
            elif t_amount > 20000000:
                BigType = 400
            elif t_amount > 10000000:
                BigType = 300
            elif t_amount > 5000000:
                BigType = 250
            elif t_amount > 2000000:
                BigType = 220
            elif t_amount > 1000000:
                BigType = 210
            elif t_amount > 500000:
                BigType = 205
            elif t_amount > 200000:
                BigType = 202
            elif t_amount > 100000:
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
                BigAmount.trade_value = t_amount
                BigAmount.trade_status = t_style
                session.merge(BigAmount)
            
            #calculate price table
            PriceDictCount[t_price] = PriceDictCount.setdefault(t_price, 0) + t_count
            PriceDictAmount[t_price] = PriceDictAmount.setdefault(t_price, 0) + t_amount
            if t_style == 1:
                BuyPriceDictCount[t_price] = BuyPriceDictCount.setdefault(t_price, 0) + t_count
                BuyPriceDictAmount[t_price] = BuyPriceDictAmount.setdefault(t_price, 0) + t_amount
            elif t_style == 2:
                SellPriceDictCount[t_price] = SellPriceDictCount.setdefault(t_price, 0) + t_count
                SellPriceDictAmount[t_price] = SellPriceDictAmount.setdefault(t_price, 0) + t_amount
            
            if BigType != 0:
                BigPriceDictCount[BigType][t_price] = BigPriceDictCount[BigType].setdefault(t_price, 0) + t_count
                BigPriceDictAmount[BigType][t_price] = BigPriceDictAmount[BigType].setdefault(t_price, 0) + t_amount
                if t_style == 1:
                    BigBuyPriceDictCount[BigType][t_price] = BigBuyPriceDictCount[BigType].setdefault(t_price, 0) + t_count
                    BigBuyPriceDictAmount[BigType][t_price] = BigBuyPriceDictAmount[BigType].setdefault(t_price, 0) + t_amount
                elif t_style == 2:
                    BigSellPriceDictCount[BigType][t_price] = BigSellPriceDictCount[BigType].setdefault(t_price, 0) + t_count
                    BigSellPriceDictAmount[BigType][t_price] = BigSellPriceDictAmount[BigType].setdefault(t_price, 0) + t_amount
        
        #calculate price variation
        last_day = session.query(StockDailyRecord).filter(StockDailyRecord.stock_id == stockid).order_by(StockDailyRecord.trade_date.desc()).first()
        
        max_diff = high_price - low_price
        if last_day != None:
            last_price = last_day.end_price
            variation = end_price - last_price
            variat_rate = round(variation / last_price, 4) * 100
            amplitude = round(max_diff / last_price, 4) * 100
        exchange_rate = round(float(trade_count) * 100 / ATradeShare, 6) * 100
        buy_rate = round(float(buy_count) * 100 / ATradeShare, 6) * 100
        sell_rate = round(float(sell_count) * 100 / ATradeShare, 6) * 100
        neutral_rate = round(float(neutral_count) * 100 / ATradeShare, 6) * 100
        
        SDR = StockDailyRecord()
        SDR.stock_id = stockid
        SDR.trade_date = datadate
        SDR.init_price = init_price
        SDR.end_price = end_price
        SDR.high_price = high_price
        SDR.low_price = low_price
        SDR.variation = variation
        SDR.variat_rate = variat_rate
        SDR.amplitude = amplitude
        SDR.trade_amount = trade_amount
        SDR.trade_count = trade_count
        SDR.exchage_rate = exchange_rate
        SDR.buy_amount =buy_amount
        SDR.buy_count = buy_count
        SDR.buy_rate = buy_rate
        SDR.sell_amount = sell_amount
        SDR.sell_count = sell_count
        SDR.sell_rate = sell_rate
        SDR.neutral_amount = neutral_amount
        SDR.neutral_count = neutral_count
        SDR.neutral_rate = neutral_rate        
        session.merge(SDR)
        
        #save price table to DB
        
        
        '''tbl_name = 'BigDailyPriceTable' + stockid[-1] + '()'
        BDPT = eval(tbl_name)
        tbl_name = 'BigBuyDailyPriceTable' + stockid[-1] + '()'
        BBDPT = eval(tbl_name)
        tbl_name = 'BigSellDailyPriceTable' + stockid[-1] + '()'
        BSDPT = eval(tbl_name)'''

        for price in PriceDictCount:
            tbl_name = 'DailyPriceTable' + stockid[-1] + '()'
            DPT = eval(tbl_name)
            DPT.stock_id = stockid
            DPT.trade_date = datadate
            DPT.price = price
            DPT.count = PriceDictCount[price]
            DPT.amount = PriceDictAmount[price]
            session.merge(DPT)
        
        for price in BuyPriceDictCount:
            tbl_name = 'BuyDailyPriceTable' + stockid[-1] + '()'
            BDPT = eval(tbl_name)
            BDPT.stock_id = stockid
            BDPT.trade_date = datadate
            BDPT.price = price
            BDPT.count = BuyPriceDictCount[price]
            BDPT.amount = BuyPriceDictAmount[price]
            session.merge(BDPT)
        
        for price in SellPriceDictCount:
            tbl_name = 'SellDailyPriceTable' + stockid[-1] + '()'
            SDPT = eval(tbl_name)
            SDPT.stock_id = stockid
            SDPT.trade_date = datadate
            SDPT.price = price
            SDPT.count = SellPriceDictCount[price]
            SDPT.amount = SellPriceDictAmount[price]
            session.merge(SDPT)
        
        for i in xrange(len(BigTypes)):
            now_name = BigTypes[i]
            if i > 0:
                last_name = BigTypes[i-1]
                for key in BigPriceDictCount[last_name]:
                    BigPriceDictCount[now_name][key] = BigPriceDictCount[now_name].setdefault(key,0) + BigPriceDictCount[last_name][key]
                    BigPriceDictAmount[now_name][key] = BigPriceDictAmount[now_name].setdefault(key,0) + BigPriceDictAmount[last_name][key]
                for key in BigSellPriceDictCount[last_name]:
                    BigSellPriceDictCount[now_name][key] = BigSellPriceDictCount[now_name].setdefault(key,0) + BigSellPriceDictCount[last_name][key]
                    BigSellPriceDictAmount[now_name][key] = BigSellPriceDictAmount[now_name].setdefault(key,0) + BigSellPriceDictAmount[last_name][key]
                for key in BigBuyPriceDictCount[last_name]:
                    BigBuyPriceDictCount[now_name][key] = BigBuyPriceDictCount[now_name].setdefault(key,0) + BigBuyPriceDictCount[last_name][key] 
                    BigBuyPriceDictAmount[now_name][key] = BigBuyPriceDictAmount[now_name].setdefault(key,0) + BigBuyPriceDictAmount[last_name][key]
            
            for price in BigPriceDictCount[now_name]:
                tbl_name = 'BigDailyPriceTable' + stockid[-1] + '()'
                BDPT = eval(tbl_name)
                BDPT.stock_id = stockid
                BDPT.trade_date = datadate
                BDPT.price = price
                BDPT.count = BigPriceDictCount[now_name][price]
                BDPT.amount = BigPriceDictAmount[now_name][price]
                BDPT.big_type = now_name
                session.merge(BDPT)
            
            for price in BigSellPriceDictCount[now_name]:
                tbl_name = 'SellBigDailyPriceTable' + stockid[-1] + '()'
                SBDPT = eval(tbl_name)
                SBDPT.stock_id = stockid
                SBDPT.trade_date = datadate
                SBDPT.price = price
                SBDPT.count = BigSellPriceDictCount[now_name][price]
                SBDPT.amount = BigSellPriceDictAmount[now_name][price]
                SBDPT.big_type = now_name
                session.merge(SBDPT)
            
            for price in BigBuyPriceDictCount[now_name]:
                tbl_name = 'BuyBigDailyPriceTable' + stockid[-1] + '()'
                BBDPT = eval(tbl_name)
                BBDPT.stock_id = stockid
                BBDPT.trade_date = datadate
                BBDPT.price = price
                BBDPT.count = BigBuyPriceDictCount[now_name][price]
                BBDPT.amount = BigBuyPriceDictCount[now_name][price]
                BBDPT.big_type = now_name
                session.merge(BBDPT)
        
        session.commit()
        session.close()




















