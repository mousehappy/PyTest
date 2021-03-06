#coding=utf-8
import os
from DBModule.Modules import *
from sqlalchemy import or_
from sqlalchemy.sql.operators import like_op
from CrawlManager import CrawlManager
from StockDetailCrawler import StockDetailCrawler
from datetime import date, timedelta, datetime
import time
from DBModule.Modules import G_DB
from CrawlConfig import G_Config
import Utilit
from DataStorage.TokenManagement import TokenManagement
import json
import cStringIO

class CrawlServer(object):
    __DB = None
    __CrawlManager = None
    __Crawl_Finish = False
    __TM = None
    
    def __init__(self, db_con = None):
        object.__init__(self)
        self.__CrawlManager = CrawlManager()
        if db_con != None:
            self.__DB = DB_Base(db_con)
        else:
            self.__DB = G_DB
        self.__TM = TokenManagement()
        
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
        stocks = self.__TM.get_initial_token()
        stock_count = len(stocks)
        while stock_count != 0:
            task_dict = {}
            print 'start crawl stocks:',stocks
            for stock in stocks:
                task_dict.setdefault(stock, []).append(start_date)
                task_dict[stock].append(end_date)
            
            self.__CrawlManager.generate_tasks(tasks = task_dict)
            self.__CrawlManager.start_crawl()
            self.__Crawl_Finish = False
            self.waiting_for_crawl()
            error_records = self.__CrawlManager.get_errors()
            self.__TM.complete_crawl(task_dict, error_records)
            stocks = self.__TM.get_initial_token()
            stock_count = len(stocks)
        
        error_sms = self.__TM.get_error_token()
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
            self.__TM.complete_crawl(task_dict, error_records)
            error_sms = self.__TM.get_error_token()
            stock_count = len(error_sms)
        
        print "Initial crawl finished!!"
                #task_dict.setdefault(stock.id, []).append()
    
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
            
    def check_stock_base_info(self):
        session = self.__DB.get_session()
        SDC = StockDetailCrawler()
        #Crawl detail of sh stocks
        stocks = session.query(StockManagement).filter(StockManagement.status >= 0, StockManagement.market == 'sh').all()
        invalid_stocks = []
        for stock in stocks:
            stockid = stock.id      
            result = ''
            if stockid[0] == '9':
                invalid_stocks.append(stockid)
                continue
            result = SDC.crawl_sh_base_info(stockid)

            if result == False or result['STATE_CODE_A_DESC'] != '上市':
                invalid_stocks.append(stockid)
            else:
                csrc_cate = result["CSRC_CODE_DESC"]
                csrc_mid_cate =result["CSRC_GREAT_CODE_DESC"]
                csrc_sub_cate = result["CSRC_MIDDLE_CODE_DESC"]
                
                stock_csrc1 = CSRCCategory()
                if len(csrc_cate) > 0 and csrc_cate != '-': 
                    stock_csrc1.cate_type = 1
                    stock_csrc1.name = csrc_cate
                    stock_csrc1 = session.merge(stock_csrc1)
                    session.commit()
                
                stock_csrc2 = CSRCCategory()
                if len(csrc_mid_cate) > 0 and csrc_mid_cate != '-':
                    stock_csrc2.cate_type = 2
                    stock_csrc2.name = csrc_mid_cate
                    stock_csrc2.parent_cate = stock_csrc1.id
                    stock_csrc2 = session.merge(stock_csrc2)
                    session.commit()
                
                
                stock_csrc3 = CSRCCategory()
                if len(csrc_sub_cate) > 0 and csrc_sub_cate != '-':
                    stock_csrc3.cate_type = 2
                    stock_csrc3.name = csrc_sub_cate
                    stock_csrc3.parent_cate = stock_csrc2.id
                    session.merge(stock_csrc3)
                    session.commit()
                
                stock_sse = SSECategory()
                stock_sse_cate = result['SSE_CODE_DESC']
                if len(stock_sse_cate) > 0 and stock_sse_cate != '-':
                    stock_sse.name = stock_sse_cate
                    session.commit()
                    
                stock_base = StockBaseInfo()
                stock_base.id = stockid
                stock_base.area = result['AREA_NAME_DESC']
                stock_base.name = result['COMPANY_ABBR']
                stock_base.Astatus = result['STATE_CODE_A_DESC']
                stock_base.Bstatus = result['STATE_CODE_B_DESC']
                stock_base.total_rate = result['totalSharesPercent']
                stock_base.total_share = float(result['totalShares'])*10000
                stock_base.tradable_rate = result['totalFlowSharesPercent']
                stock_base.tradable_share = float(result['totalFlowShares'])*10000
                stock_base.nontradable_rate = result['totalNonFlowSharePercent']
                stock_base.nontradable_share = float(result['totalNonFlowShare'])*10000
                stock_base.csrc_main_cate = stock_csrc1.id
                stock_base.csrc_mid_cate = stock_csrc2.id
                stock_base.csrc_sub_cate = stock_csrc3.id
                if result.has_key('LISTINGDATEA'):
                    stock_base.IPODate = datetime.strptime(result['LISTINGDATEA'], '%Y-%m-%d').date()
                   
                stock_base = session.merge(stock_base)
                session.commit()
        
        for stock in invalid_stocks:
            SM = StockManagement()
            SM.id = stock
            SM.status = -3
            SM = session.merge(SM)
            
        session.commit()
        
        # Crawl detail of sz stocks
        invalid_stocks = []
        stocks = session.query(StockManagement.id).filter(StockManagement.status >= 0, StockManagement.market == 'sz').all()
        invalid_stock_set = set()
        for stock in stocks:
            invalid_stock_set.add(stock[0])
            
        stocks = SDC.crawl_sz_base_info()
        for stock in stocks:
            #stockid,stockname,Ashare,Atradableshare,area,csrc
            stockid = stock[0]
            invalid_stock_set.discard(stockid)
            
            if Utilit.ConvertStringToInt(stock[2]) == 0:
                invalid_stocks.append(stockid)
                continue
            
            stock_csrc1 = CSRCCategory()
            stock_csrc1.name = stock[5]
            stock_csrc1 = session.merge(stock_csrc1)
            session.commit()
            
            stock_base = StockBaseInfo()
            stock_base.id = stockid
            stock_base.name = stock[1]
            stock_base.total_share = Utilit.ConvertStringToInt(stock[2])
            stock_base.tradable_share = Utilit.ConvertStringToInt(stock[3])
            stock_base.Astatus = '上市'
            stock_base.area = stock[4]
            stock_base.csrc_main_cate = stock_csrc1.id
            stock_base.IPODate = stock[6]
            stock_base = session.merge(stock_base)
            
        session.commit()
        
        for stockid in invalid_stock_set:
            invalid_stocks.append(stockid)
            
        for stock in invalid_stocks:
            SM = StockManagement()
            SM.id = stock
            SM.status = -3
            SM = session.merge(SM)
            
        session.commit()
        session.close()
    
    def finance_initial_crawl(self):
        from iCaifuCrawler import iCaifuCrawler
        from DBModule.Modules import StockFinanceStatement
        stocks = self.__TM.get_initial_finance()
        iCF = iCaifuCrawler()
        Today = date.today()
        year = Today.year
        success_stocks = set()
        limit_reach = False
        if len(stocks) > 0:
            for stock in stocks:
                content = iCF.CrawlFinaceIndex(stock[0], stock[1], year)
                if content == False:
                    continue
                
                content = json.load(cStringIO.StringIO(content))
                retcode = content['retcode']
                if retcode == 1006:
                    time.sleep(5)
                    continue
                elif retcode == 1009:
                    continue
                elif retcode == 1007:
                    limit_reach = True
                    break
                
                stock_id = stock[0]
                stock_market = stock[1]
                finance_list = content['finance_index']
                session = self.__DB.get_session()
                '''SM =StockManagement()
                SM.id = stock_id
                SM.status += 200
                SM = session.merge(SM)
                session.commit()
                print SM.id, SM.status'''
                stmt = session.query(StockManagement).filter(StockManagement.id == stock_id).one()
                stmt.status = stmt.status + 200
                session.commit()
                session.close()
                #stmt = StockManagement.update().where(StockManagement.c.id == stock_id).values(status = StockManagement.c.status + 200)
                #stmt.excute()
                    
