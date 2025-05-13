from typing import Optional
from pydantic import BaseModel, field_validator


class BasketInput(BaseModel):
    
    products: Optional[str] = ""
    
    @field_validator('products', mode='after')
    @classmethod
    def validate_x(cls, products: str) -> str:
        if products == "":
            return products
        if not products.isalpha():
            raise ValueError('Invalid input provided')
        return products.upper()