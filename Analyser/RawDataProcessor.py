from DBModule.Modules import G_DB
from datetime import date, timedelta

class RawDataProcessor:
    def __init__(self):
        pass
    
    def CalculateStatus(self, stockid, now_date):
        session = G_DB.get_session()
        
    def VolumeAmplified(self, idate, ifactor):
        last_date = idate - timedelta(1)
        for i in xrange(10):
            