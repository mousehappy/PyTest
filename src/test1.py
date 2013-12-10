from CrawlServer.Crawler.StockListCrawler import StockListCrawler

print 'start crawl!!'
scrawler = StockListCrawler();
scrawler.crawl()

print scrawler.get_stock_list()