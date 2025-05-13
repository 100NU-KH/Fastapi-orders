from enum import Enum


class ConditionalOfferStatus(Enum):
    
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ConditionType(Enum):
    
    COUNT = 'COUNT'
    VALUE = 'VALUE'
    

class BenefitType(Enum):
    FIXED_PRICE = 'FIXED-PRICE'
    PERCENTAGE = 'PERCENTAGE'
    
    