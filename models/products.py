from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base

from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, default=0.0)
    
    conditional_offer_id = Column(
        Integer,
        ForeignKey('conditional_offer.id'),
        nullable=True
    )
    
    conditional_offer = relationship('ConditionalOffers', back_populates='products')