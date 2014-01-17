from DBModule.Modules import *
from DBModule.DailyPriceTable import *
from DBModule.BigDailyPriceTable import *


G_Base.metadata.create_all(G_DB.get_engine())