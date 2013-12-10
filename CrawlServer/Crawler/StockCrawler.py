class StockCrawler:
    def __init__(self):
        self.a = 1
        print "StockCrawler is initializing!!"
    
    def add_one(self):
        self.a = self.a + 1
    
    def __str__(self):
        return str(self.a)
    
    def __repr__(self):
        return repr(self.a)