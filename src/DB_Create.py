from DBModule.Modules import *

DB = DB_Base("mysql://root:admin@localhost:3306/MyStock?charset=utf8")

Base = DB.get_base()

Base.metadata.create_all(DB.get_engine())