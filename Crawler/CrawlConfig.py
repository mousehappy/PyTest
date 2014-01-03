
class CrawlConfig:
    db_str = ""
    db_args = {}
    data_dir = ""
    def __init__(self):
        self.db_str = "mysql://root:admin@localhost:3306/MyStock?charset=utf8&use_unicode=0"
        self.data_dir = "~/StockData"
        #self.db_args["convert_unicode"] = True
        #self.db_args["encoding"] = 'utf-8'

G_Config = CrawlConfig()