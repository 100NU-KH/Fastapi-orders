from typing import Optional, List, Union
from pydantic import BaseModel, field_validator, PositiveInt, PositiveFloat, ConfigDict

from database import get_db
from models import ConditionalOffers, Products
from schemas.conditionaloffers import ConditionalOfferDetail


class CreateProduct(BaseModel):
    
    name: str
    price: PositiveFloat
    conditional_offer_ids: List[Optional[PositiveInt]] = []
    
    @field_validator('conditional_offer_ids', mode='after')
    @classmethod
    def validate_conditional_offer_ids(cls, conditional_offer_ids: int) -> list:
        if conditional_offer_ids:
            db = next(get_db())
            if not db.query(ConditionalOffers).filter(
                    ConditionalOffers.id.in_(conditional_offer_ids)
                ).count() == len(conditional_offer_ids):
                raise ValueError("Conditional Offer with provided ID does not exists")
        return conditional_offer_ids
    
    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, name: str) -> Union[str, ValueError]:
        db = next(get_db())
        if db.query(Products).filter(Products.name==name).first():
            raise ValueError("Product with same name already exists.")
        return name
class ProductDetails(BaseModel):
    
    id: int
    name: str
    price: PositiveFloat
    conditional_offers: Optional[List[ConditionalOfferDetail]] = None
    