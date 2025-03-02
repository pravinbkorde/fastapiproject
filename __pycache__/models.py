from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func 
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum("finished", "semi-finished", "raw"), nullable=False)
    description = Column(String(250), nullable=True)
    product_image = Column(String, nullable=True)
    sku = Column(String(100), nullable=False)
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack"), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now())  
    updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now()) 
