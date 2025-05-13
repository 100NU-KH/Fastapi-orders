from pydantic import BaseModel, PositiveInt
from enums import BenefitType

class CreateBenefit(BaseModel):
    
    description: str
    typ : BenefitType
    value: float
    

class BenefitDetails(BaseModel):
    id: int
    description: str
    typ: BenefitType
    value: float
    is_active: bool