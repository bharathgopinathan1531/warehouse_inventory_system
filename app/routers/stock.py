from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user

from app.database import SessionLocal
from app.models import Product, StockHistory
from app.schemas import StockUpdate

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/inward")
def add_stock(
    stock: StockUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    product = db.query(Product).filter(
        Product.id == stock.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.stock_quantity += stock.quantity
    
    history = StockHistory(
    product_id=product.id,
    movement_type="IN",
    quantity=stock.quantity
)
    db.add(history)
    db.commit()

    return {
        "message": "Stock added successfully",
        "new_stock": product.stock_quantity
    }

@router.post("/outward")
def remove_stock(
    stock: StockUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    product = db.query(Product).filter(
        Product.id == stock.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.stock_quantity < stock.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    product.stock_quantity -= stock.quantity
    
    history = StockHistory(
    product_id=product.id,
    movement_type="OUT",
    quantity=stock.quantity
)
    db.add(history)
    db.commit()

    return {
        "message": "Stock removed successfully",
        "new_stock": product.stock_quantity
    }


@router.get("/")
def get_stock(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    products = db.query(Product).all()
    return products

@router.get("/low")
def low_stock(
    db: Session = Depends(get_db)
):
    products = db.query(Product).filter(
        Product.stock_quantity < 5
    ).all()

    return products

@router.get("/history")
def stock_history(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    history = db.query(StockHistory).all()
    return history