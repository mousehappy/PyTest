#from Crawler.CrawlConfig import G_Config
from Crawler.StockDetailCrawler import StockDetailCrawler
from Crawler.CrawlServer import CrawlServer
import os
import platform
import sys

d = {}

d['wsz'] = d.setdefault('wsz',0) + 20
d['wsz'] = d.setdefault('wsz',0) + 10

CS = CrawlServer()

CS.check_stock_base_info()

print d['wsz']