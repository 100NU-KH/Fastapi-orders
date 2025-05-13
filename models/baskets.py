from database import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Baskets(Base):
    
    __tablename__ = 'baskets'
    
    total = Column(Float, default=0.0)
    net_total = Column(Float, default=0.0)
    discount = Column(Float, default=0.0)
    

class BasketLines(Base):
    
    __tablename__ = 'basket_lines'
    
    basket_id = Column(
        Integer,
        ForeignKey('baskets.id'),
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        nullable=False
    )
    quantity = Column(
        Integer,
        nullable=False
    )
    
    