from Crawler.CrawlConfig import G_Config
from Crawler.StockDetailCrawler import StockDetailCrawler
from test.test_iterlen import len
from lxml import etree
from Crawler.CrawlServer import CrawlServer

CS = CrawlServer()

CS.check_stock_base_info()