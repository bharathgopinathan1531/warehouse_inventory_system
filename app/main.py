from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, products
from app.routers import suppliers
from app.routers import stock
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse Inventory Management System",
    description="Inventory Management API with Authentication, Products, Suppliers and Stock Tracking",
    version="1.0.0"
)

app.include_router(auth.router)

app.include_router(products.router)

app.include_router(suppliers.router)

app.include_router(stock.router)

@app.get("/")
def home():
    return {"message": "Warehouse Inventory System"}