from pydantic import BaseModel, EmailStr, Field
from typing import Literal

# User
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Literal["Admin","Staff"]


class UserLogin(BaseModel):
    username: str
    password: str


# Product
class ProductCreate(BaseModel):
    product_name: str
    sku: str
    category: str
    price: int = Field(..., gt=0)
    stock_quantity: int


# Supplier
class SupplierCreate(BaseModel):
    supplier_name: str
    email: str
    phone: str
    

# Stock
class StockUpdate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)   
    
# ProductUpdate
class ProductUpdate(BaseModel):
    product_name: str
    sku: str
    category: str
    price: int
    stock_quantity: int    