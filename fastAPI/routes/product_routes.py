from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app_db import get_db
import app_models
import schemas
import crud


router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[schemas.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(app_models.Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(app_models.Product).filter(app_models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=schemas.ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session =Depends(get_db)):
    return crud.create_product(db,product)
