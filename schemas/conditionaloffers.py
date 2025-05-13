from pydantic import BaseModel, field_validator, model_validator, PositiveInt, PositiveFloat
from enums import ConditionType

from fastapi import Depends
from models import ConditionalOffers, Conditions, Benefits
from database import get_db
from schemas.benefits import BenefitDetails

class CreateCondition(BaseModel):
    
    description: str
    typ: ConditionType
    value: float
    
    
class ConditionsDetails(BaseModel):
    
    id: int
    description: str
    typ: ConditionType
    value: float
    is_active: bool
    

class CreateConditionalOffer(BaseModel):
    
    name: str
    status: str
    condition_id: PositiveInt
    benifit_id: PositiveInt
    
    @field_validator('name', mode='after')
    @classmethod
    def validate_x(cls, name: str) -> str:
        db = next(get_db())
        if db.query(ConditionalOffers).filter(
                ConditionalOffers.name==name
            ).first():
            raise ValueError("'name' already exists.")
        return name
    
    @model_validator(mode='after')
    def validateForeignIds(self):
        db = next(get_db())
        if not db.query(Conditions).filter(
                Conditions.id==self.condition_id
            ).first():
            raise ValueError("Invalid 'id' for Conditions. Object Does not exists with the provided ID")
        if not db.query(Benefits).filter(
                Benefits.id==self.benifit_id
            ).first():
            raise ValueError("Invalid 'id' for Benefits. Object Does not exists with the provided ID")
        
        return self

class ConditionalOfferDetail(BaseModel):
    
    id: int
    name: str
    status: str
    condition: ConditionsDetails
    benifit: BenefitDetails