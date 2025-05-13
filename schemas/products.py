from typing import Optional
from pydantic import BaseModel, field_validator, PositiveInt, PositiveFloat

from database import get_db
from models import ConditionalOffers
from schemas.conditionaloffers import ConditionalOfferDetail


class CreateProduct(BaseModel):
    
    name: str
    price: PositiveFloat
    conditional_offer_id: Optional[PositiveInt] = None
    
    @field_validator('conditional_offer_id', mode='after')
    @classmethod
    def validate_x(cls, conditional_offer_id: int) -> str:
        if conditional_offer_id:
            db = next(get_db())
            if not db.query(ConditionalOffers).filter(
                    ConditionalOffers.id==conditional_offer_id
                ).first():
                raise ValueError("Conditional Offer with provided ID does not exists")
        return conditional_offer_id
    
class ProductDetails(BaseModel):
    
    id: int
    name: str
    price: PositiveFloat
    conditional_offer: Optional[ConditionalOfferDetail] = None
    