from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models.products import Products
from schemas.basket import BasketInput
from collections import Counter

router = APIRouter(
    prefix='/basket',
    tags=['Basket']
)


@router.post('/')
def calculate_basket_price(request: BasketInput, db: Session= Depends(get_db)):
    basket_total = 0
    counter = Counter(request.products)
    for key in counter:
        product_obj = db.query(Products).filter(Products.name==key).first()
        offer = product_obj.conditional_offer
        if  offer and product_obj and offer.status == "ACTIVE" and offer.condition.typ == 'COUNT' \
            and counter[key] >= offer.condition.value:
                
                special_count = int(counter[key]/offer.condition.value)
                basket_total += special_count * offer.benifit.value

                normal_count = int(counter[key] % offer.condition.value)
                if normal_count:
                    basket_total += normal_count * product_obj.price
        else:
            basket_total += counter[key] * product_obj.price
    return int(basket_total)