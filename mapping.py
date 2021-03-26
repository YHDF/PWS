from sqlalchemy import *
from sqlalchemy.orm import declarative_base


engine = create_engine('mysql://localhost:3306/Testing?user=root&password=yh', echo=True)
Base = declarative_base()
class Product(Base):
         __tablename__ = 'products'

         id = Column(String, primary_key=True)
         name = Column(String)
         link = Column(String)
         img_link = Column(String)
         price = Column(String)
         def __repr__(self):
             return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

print(Product.__table__)
