from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import List
from database import get_db
from models.products import Products
from models.conditional_offers import ConditionalOffers
from schemas import CreateProduct
from schemas.products import ProductDetails


router = APIRouter(
    prefix='/product',
    tags=['Products']
)

@router.get('/', response_model=List[ProductDetails])
def get_all_products(db: Session = Depends(get_db)):
    product_objs = db.query(Products).filter(Products.is_active==True).all()
    return product_objs

@router.post('/create')
def create_product(request: CreateProduct, db: Session = Depends(get_db)):
    new_product = Products(
        name=request.name,
        price=request.price
    )
    if request.conditional_offer_ids:
        for conditional_offer_id in request.conditional_offer_ids:
            conditional_off_obj = db.query(ConditionalOffers).filter(ConditionalOffers.id==conditional_offer_id).first()
            if conditional_off_obj:
                new_product.conditional_offers.append(conditional_off_obj)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product