from DBModule.Modules import *

session = G_DB.get_session()

SMs = session.query(StockManagement).limit(100).all()

for SM in SMs:
    print SM
