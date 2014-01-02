from Crawler.CrawlConfig import G_Config

def testparam(db_str, **args):
    print db_str
    print args
    
testparam(G_Config.data_dir, encoding='latin1', echo=True)