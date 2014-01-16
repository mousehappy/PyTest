
class CrawlConfig:
    db_str = ""
    db_args = {}
    data_dir = ""
    def __init__(self):
        self.db_str = "mysql://root:admin@localhost:3306/MyStock?charset=utf8&use_unicode=0"
<<<<<<< HEAD
        self.data_dir = "/Users/shwang/StockData"
=======
        self.data_dir = "C:\\StockData"
>>>>>>> ec6bf42550f8595a9e8f61c26dcc7b6eff52fa15
        #self.db_args["convert_unicode"] = True
        #self.db_args["encoding"] = 'utf-8'

G_Config = CrawlConfig()