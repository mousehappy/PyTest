from Crawler.CrawlServer import CrawlServer
CS = CrawlServer()

<<<<<<< HEAD:src/test2.py
CS.set_database('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
CS.inital_crawl(1000)
=======
#CS.set_database('mysql://root:admin@localhost:3306/MyStock?charset=utf8')
CS.inital_crawl(4000)
>>>>>>> ec6bf42550f8595a9e8f61c26dcc7b6eff52fa15:test2.py

#CS.test_error_crawl()  

#error_count = CS.get_all_error_token()


CS.print_tasks()




