import sys
import pycurl

filename = 'stockdata'
url = 'http://market.finance.sina.com.cn/downxls.php?date=2013-12-09&symbol=sz002363'
#url = 'http://www.163.com'
fp = open(filename, "wb")
curl = pycurl.Curl()
curl.setopt(pycurl.URL, url)
curl.setopt(pycurl.FOLLOWLOCATION, 1)
curl.setopt(pycurl.MAXREDIRS, 5)
curl.setopt(pycurl.CONNECTTIMEOUT, 30)
curl.setopt(pycurl.TIMEOUT, 300)
curl.setopt(pycurl.NOSIGNAL, 1)
curl.setopt(pycurl.WRITEDATA, fp)
curl.perform()

curl.close()
fp.close()
sys.stdout.write(".")
sys.stdout.flush()