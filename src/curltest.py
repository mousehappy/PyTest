import pycurl
import cStringIO
import json

base_url = 'http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonp1&isPagination=false&sqlId=COMMON_SSE_ZQPZ_GP_GPLB_AGSSR_C&productid=600000'
refer = 'http://www.sse.com.cn/assortment/stock/list/stockdetails/company/index.shtml?COMPANY_CODE=600000'

buf = cStringIO.StringIO()
curl = pycurl.Curl()
curl.setopt(pycurl.URL, base_url)
if refer:
    curl.setopt(pycurl.REFERER, refer)
curl.setopt(pycurl.FOLLOWLOCATION, 1)
curl.setopt(pycurl.MAXREDIRS, 5)
curl.setopt(pycurl.CONNECTTIMEOUT, 30)
curl.setopt(pycurl.TIMEOUT, 300)
curl.setopt(pycurl.NOSIGNAL, 1)
curl.setopt(pycurl.WRITEFUNCTION, buf.write)

curl.perform()


base_data = buf.getvalue()
ofile = open('curltest.txt','w+')
ofile.write(base_data)
ofile.close()
base_data = base_data[7:-1]
base_data = json.load(cStringIO.StringIO(base_data))
base_result = base_data["result"][0]

for key in base_result.keys():
    print key