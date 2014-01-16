import sys
import pycurl
import cStringIO
import json
import datetime
from lxml import etree

class StockDetailCrawler:
    
    sh_refer = ''
    sh_base_url = ''
    sh_share_url = ''
    sh_IPO_url = ''
    sz_file_url = 'http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab1&ENCODE=1'
    
    def __init__(self):
        self.sh_refer = "http://www.sse.com.cn/assortment/stock/list/stockdetails/capital/index.shtml?SecurityCode=-&COMPANY_CODE="
        self.sh_base_url = "http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonp1&isPagination=false&sqlId=COMMON_SSE_ZQPZ_GP_GPLB_C&productid="
        self.sh_share_url = "http://query.sse.com.cn/security/stock/queryCompanyStockStruct.do?jsonCallBack=jsonp1&isPagination=false&companyCode="
        self.sh_IPO_url = "http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonp1&isPagination=false&sqlId=COMMON_SSE_ZQPZ_GP_GPLB_AGSSR_C&productid="
    
    def crawl_sz_base_info(self):
        buf = cStringIO.StringIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, self.sz_file_url)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.MAXREDIRS, 5)
        curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.NOSIGNAL, 1)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        for try_t in range(1,4):
            try:
                curl.perform()
            except:
                print "Crawl sz stocks base info failed with %d try"%try_t
            else:
                break
        else:
            curl.close()
            return False
        record = open('szstock','w+')
        stock_info = buf.getvalue().decode('gbk')
        record.write(stock_info)
        curl.close()
        record.close()
        
        stocks=[]
        html = etree.HTML(stock_info)
        head = html[0]
        body = html[1]
        table = body[0]
        for row in table[1:]:
            stockid = row[0].text
            stockname = row[1].text
            Ashare = row[8].text
            Atradableshare = row[9].text
            area = row[16].text
            csrc = row[18].text[2:]
            IPODate = None
            if row[7].text and len(row[7].text) > 0: 
                IPODate = datetime.datetime.strptime(row[7].text,'%Y-%m-%d').date()
            stocks.append([stockid,stockname,Ashare,Atradableshare,area,csrc,IPODate])
        return stocks
    
    def crawl_sh_base_info(self, stockid):
        #Base info of stock      
        refer = self.sh_refer + stockid
        base_url = self.sh_base_url + stockid
        share_url = self.sh_share_url + stockid
        IPO_url = self.sh_IPO_url + stockid
        
        buf = cStringIO.StringIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, base_url)
        curl.setopt(pycurl.REFERER, refer)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.MAXREDIRS, 5)
        curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.NOSIGNAL, 1)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)

        for try_t in range(1,4):
            try:
                curl.perform()
            except:
                print "Crawl base info of %s failed with %d try"%(stockid, try_t)
            else:
                break
        else:
            return False
        
        base_data = buf.getvalue()
        base_data = base_data[7:-1]
        base_data = json.load(cStringIO.StringIO(base_data))
        base_result = base_data["result"]
        
        if len(base_result) == 0:
            return False
        base_result = base_result[0]
        result = base_result
        #share info of stock
        buf = cStringIO.StringIO()
        curl.setopt(pycurl.URL, share_url)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        for try_t in range(1,4):
            try:
                curl.perform()
            except:
                print "Crawl share info of %s failed with %d try"%(stockid, try_t)
            else:
                break
        
        share_data = buf.getvalue()
        share_data = share_data[7:-1]
        share_data = json.load(cStringIO.StringIO(share_data))
        share_result = share_data["result"]
        
        if len(share_result) > 0:
            result = dict(result.items() + share_result.items())

        
        #IPO info of stock
        buf = cStringIO.StringIO()
        curl.setopt(pycurl.URL, IPO_url)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        for try_t in range(1,4):
            try:
                curl.perform()
            except:
                print "Crawl IPO info of %s failed with %d try"%(stockid, try_t)
            else:
                break
        
        IPO_data = buf.getvalue()
        IPO_data = IPO_data[7:-1]
        IPO_data = json.load(cStringIO.StringIO(IPO_data))
        IPO_result = IPO_data["result"]
        
        if len(IPO_result) > 0:
            IPO_result = IPO_result[0]
            if len(IPO_result) > 0:
                result = dict(result.items() + IPO_result.items())

        return result
