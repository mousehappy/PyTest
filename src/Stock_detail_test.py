#coding=utf-8
import sys
import pycurl
import cStringIO
from StringIO import StringIO
import json
from DBModule.Modules import *
from Crawler.StockDetailCrawler import StockDetailCrawler
from test.test_iterlen import len

filename = 'stocklist.html'
#url = 'http://www.163.com'

#url = "http://www.sse.com.cn/assortment/stock/list/stockdetails/company/index.shtml?SecurityCode=-&COMPANY_CODE=600001"

def EncodeDictWithUTF8(idict):
    for key in idict:
        if isinstance(idict[key], unicode):
            idict[key] = idict[key].encode('utf-8')
    

SDCrawler = StockDetailCrawler();
stockid = 'sh900901'
result = SDCrawler.crawl_sh_base_info(stockid)

#EncodeDictWithUTF8(result)
session = G_DB.get_session()
'''CSRC_CODE_DESC (60562032)    unicode: 金融业    
    CSRC_GREAT_CODE_DESC (60562872)    unicode: 货币金融服务    '''

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
stock_base.total_share = result['totalShares']
stock_base.tradable_rate = result['totalFlowSharesPercent']
stock_base.tradable_share = result['totalFlowShares']
stock_base.nontradable_rate = result['totalNonFlowSharePercent']
stock_base.nontradable_share = result['totalNonFlowShare']
stock_base.csrc_main_cate = stock_csrc1.id
stock_base.csrc_mid_cate = stock_csrc2.id
stock_base.csrc_sub_cate = stock_csrc3.id

stock_base = session.merge(stock_base)
session.commit()

session.close()
