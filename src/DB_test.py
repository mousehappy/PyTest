from Crawler.CrawlConfig import CrawlConfig
from DBModule.DbBase import *

'''SM = StockManager()
stocks=SM.SelectInitialStock()

for stock in stocks:
    print stock'''
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
    
Base = G_DB.get_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    addresses = relationship("Address", backref="user")

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
#Base.metadata.create_all(G_DB.get_engine())

session = G_DB.get_session()


#session.add(u1)
#session.add(a1)
#session.commit()

u2 = User()
u2.id = 3
u2.name = 'Shwang12345'

u2 = session.query(User).filter(User.id == 3).scalar()
a = u2.addresses

session.delete(a)
#session.delete(u2.addresses[0])
#session.delete(u2)
    

session.commit()

