#from Crawler.CrawlConfig import G_Config
from Crawler.StockDetailCrawler import StockDetailCrawler
from test.test_iterlen import len
from lxml import etree
#from Crawler.CrawlServer import CrawlServer
import os
import platform
import sys

print platform.system()
print platform.version()
print platform.architecture()
print sys.version
#CS = CrawlServer()

#CS.check_stock_base_info()