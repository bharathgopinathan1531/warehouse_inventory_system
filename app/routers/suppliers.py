from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user

from app.database import SessionLocal
from app.models import Supplier
from app.schemas import SupplierCreate


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db),
    current_user: str = 
    Depends(get_current_user)
):
    new_supplier = Supplier(
        supplier_name=supplier.supplier_name,
        email=supplier.email,
        phone=supplier.phone
    )

    db.add(new_supplier)
    db.commit()

    return {"message": "Supplier created successfully"}


@router.get("/")
def get_suppliers(
    db: Session = Depends(get_db),
    current_user: str = 
    Depends(get_current_user)
):
    suppliers = db.query(Supplier).all()
    return suppliers

@router.put("/{supplier_id}")
def update_supplier(
    supplier_id: int,
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    existing_supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not existing_supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    existing_supplier.supplier_name = supplier.supplier_name
    existing_supplier.email = supplier.email
    existing_supplier.phone = supplier.phone

    db.commit()

    return {"message": "Supplier updated"}

@router.delete("/{supplier_id}")
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db.delete(supplier)
    db.commit()

    return {"message": "Supplier deleted"}