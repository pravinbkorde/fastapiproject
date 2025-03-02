from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from typing import List
from database import SessionLocal  
from models import Product  

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProductBase(BaseModel):
    name: str
    category: str
    description: str
    product_image: str
    sku: str
    unit_of_measure: str
    lead_time: int

class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime


@app.get("/product/list", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products



@app.get("/product/{pid}/info", response_model=ProductResponse)
def get_product_info(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/product/add", response_model=ProductResponse)
def add_product(product: ProductBase, db: Session = Depends(get_db)):
    try:
        new_product = Product(**product.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductBase, db: Session = Depends(get_db)):
    try:
        existing_product = db.query(Product).filter(Product.id == pid).first()
        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")
        for key, value in product.model_dump().items():
            setattr(existing_product, key, value)
        db.commit()
        db.refresh(existing_product)
        return existing_product
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

