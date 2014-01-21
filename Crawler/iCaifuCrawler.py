from Utilit import MD5
from CrawlConfig import G_Config
import pycurl
import cStringIO

class iCaifuCrawler():
    def __init__(self):
        pass
    
    def CrawlFinaceIndex(self, stockid, market, year, num):
        api = 'v1/stock/finance_index'
        
        params = {}
        params['openid'] = G_Config.icaifu_id
        params['_input_charset'] = 'utf-8'
        params['_type'] = 'json'
        params['seq'] = G_Config.icaifu_seq
        params['symbol'] = stockid + '.' + market
        params['year'] = year
        params['type'] = num
        
        sortd_params = self.SortParams(params)
        
        sign = MD5(sortd_params+G_Config.icaifu_token)
        param_str = sortd_params + '&' + 'sign_type=MD5'
        param_str += '&' + 'sign=' + sign
        
        return self.HttpRequest(api, param_str)
        
    
    def HttpRequest(self, api, params):
        url = G_Config.icaifu_url + api + '?' + params
        buf = cStringIO.StringIO()
        curl = pycurl.Curl()
        
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.MAXREDIRS, 5)
        curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        curl.setopt(pycurl.TIMEOUT, 300)
        curl.setopt(pycurl.NOSIGNAL, 1)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        
        for try_i in range(3):
            try:
                curl.perform()
            except:
                print "Crawl finace data faild for url:%s, with try time:%s"%(url, try_i)
            else:
                content = buf.getvalue()
                return content
                break
        else:
            print "Crawl finace data faild for url:%s after 3 trys"%url
            return False
    
    def SortParams(self, dict):
        sorted_params = [(k,dict[k]) for k in sorted(dict.keys())]
        result = ""
        for item in sorted_params:
            result += item[0] + "=" + str(item[1]) + "&"
        return result[0:-1]

if __name__ == '__main__':
    iCFC = iCaifuCrawler()
    iCFC.CrawlFinaceIndex('002285', 'sz', 2013, 3)
    