
class CrawlConfig:
    db_str = ""
    data_dir = ""
    def __init__(self):
        self.db_str = "mysql://root:admin@localhost:3306/MyStock?charset=utf8"
        self.data_dir = "~/StockData"

G_Config = CrawlConfig()