from Crawler.CrawlServer import CrawlServer
CS = CrawlServer()

#CS.set_database('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
CS.inital_crawl(4000)

error_count = CS.get_all_error_token()


CS.print_tasks()




