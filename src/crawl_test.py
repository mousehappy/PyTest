from CrawlServer.Crawler.StockListCrawler import StockListCrawler
from mimify import File
from test.test_decimal import file

crawler = StockListCrawler()

crawler.crawl()

_file = open('StockList.txt','w')

for stockid in sorted(crawler.get_stock_list()):
    print stockid
    _file.write(str(stockid)+'\n')
    
_file.close()
