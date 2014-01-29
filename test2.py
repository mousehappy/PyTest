from Crawler.CrawlServer import CrawlServer
CS = CrawlServer()

#CS.set_database('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
CS.inital_crawl(1000)

#CS.test_error_crawl()  

#error_count = CS.get_all_error_token()


CS.print_tasks()




