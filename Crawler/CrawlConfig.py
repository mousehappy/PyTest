import platform
from Cython.Compiler.Naming import self_cname

class CrawlConfig:
    db_str = ""
    db_args = {}
    data_dir = ""
    icaifu_url = ""
    icaifu_id = ""
    icaifu_token = ""
    icaifu_seq = ""
    def __init__(self):
        self.db_str = "mysql://root:admin@localhost:3306/MyStock?charset=utf8&use_unicode=0"
        system = platform.system()
        if system == 'Windows':
            self.data_dir = "C:\\StockData"
        else:
            self.data_dir = "/Users/shwang/StockData"
            
<<<<<<< HEAD
        self.token_limit = 5

=======
        self.icaifu_url = "http://api.icaifu.com/"
        self.icaifu_id = "mousehappy"
        self.icaifu_token = "s0y2x971bfcvggl75ez"
        self.icaifu_seq = 12
>>>>>>> a8971330a9f3e56a902b5d14f17489115b3f215a
        #self.db_args["convert_unicode"] = True
        #self.db_args["encoding"] = 'utf-8'

G_Config = CrawlConfig()