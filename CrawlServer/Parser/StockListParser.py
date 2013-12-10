from HTMLParser import HTMLParser
import re

class StockListParser(HTMLParser):
    def __init__(self):
        self.start_a = False
        self.StockList = []
        self.encoder = ""
        HTMLParser.__init__(self)
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.start_a = True
        if tag == 'meta':
            for attr in attrs:
                if attr[0] == 'content':
                    str = re.findall('charset=\w+;?', attr[1])[0]
                    if len(str) > 0:
                        str = str[8:]
                        str.strip(';').strip();
                        self.encoder = str
    
    def handle_endtag(self, tag):
        if tag == 'a':
            self.start_a = False
            
    def handle_data(self, data):
        if self.encoder == "":
            return
        if self.start_a :
            data = data.decode(self.encoder).encode('utf8')
            if re.match('.*\(\d{6}\)', data):
                self.StockList.extend(re.findall('\d{6}', data))
    
    def get_stock_list(self):
        return self.StockList