from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    sku = Column(String, unique=True)
    category = Column(String)
    price = Column(Integer)
    stock_quantity = Column(Integer, default=0)


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String)
    email = Column(String)
    phone = Column(String)    
    
class StockHistory(Base):
    __tablename__ = "stock_history"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    movement_type = Column(String)
    quantity = Column(Integer)    