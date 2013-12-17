from DBModule.Modules import StockManagement
from DBModule.Modules import DB_Base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

DB = DB_Base('mysql://root:admin@localhost:3306/MyStock')
Base = DB.get_base()

session = DB.get_session()

Base.metadata.create_all(DB.get_engine())

session.add(StockManagement('1111','1111'))
session.add(StockManagement('2222','2222'))

session.commit()