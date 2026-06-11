from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate,ProductUpdate
from app.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    new_product = Product(
        product_name=product.product_name,
        sku=product.sku,
        category=product.category,
        price=product.price,
        stock_quantity=product.stock_quantity
    )

    db.add(new_product)
    db.commit()

    return {"message": "Product created successfully"}

@router.get("/")
def get_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    products = db.query(Product).offset(skip).limit(limit).all
    return products

@router.get("/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    return product

@router.put("/{product_id}")
def update_product(
    product_id: int,
    updated_product: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    product.product_name = updated_product.product_name
    product.sku = updated_product.sku
    product.category = updated_product.category
    product.price = updated_product.price
    product.stock_quantity = updated_product.stock_quantity

    db.commit()

    return {"message": "Product updated successfully"}

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}

@router.get("/search")
def search_product(
    name: str,
    db: Session = Depends(get_db)
):
    products = db.query(Product).filter(
        Product.product_name.contains(name)
    ).all()

    return products

@router.get("/category/{category}")
def get_products_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    products = db.query(Product).filter(
        Product.category == category
    ).all()

    return products