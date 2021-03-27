from sqlalchemy import *
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql://localhost:3306/Testing?user=root&password=yh', echo=True)
Base = declarative_base()
class Products(Base):
         __tablename__ = 'products'

         id = Column(String,nullable=False, primary_key=True)
         group_id = Column(Integer)
         name = Column(String)
         link = Column(String)
         image = Column(String)
         price = Column(Integer)
         Base.metadata.create_all(engine)
