from CrawlServer.Crawler.CrawlServer import CrawlServer

CS = CrawlServer()

CS.set_database('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
CS.inital_crawl(7)

CS.waiting_for_crawl()

CS.print_tasks()




