from Crawler.CrawlManager import CrawlManager
import time

CM = CrawlManager()

CM.set_crawl_scope('2013-12-06','2013-12-15')

CM.generate_tasks('sz002363')

CM.start_crawl()

while True:
    thread_count = CM.get_alive_crwaler()
    print "%d crwalers are alive!"%thread_count
    if thread_count == 0:
        break
    time.sleep(5)
    
print "Crawl finish!"

