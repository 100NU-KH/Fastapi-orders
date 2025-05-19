import models.conditional_offers
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from database import Base
from typing import List
from sqlalchemy.orm import relationship, Mapped

import models

class ProductConOfferM2M(Base):
    __tablename__ = 'products_condition_off_m2m_link'
    
    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        nullable=False
    )
    conditional_offer_id = Column(
        Integer,
        ForeignKey('conditional_offer.id'),
        nullable=False
    )

# this is the alrernate declaration of the above associated table
# product_conditional_off_m2m_link = Table(
#     'products_condition_off_m2m_link', Base.metadata,
#     Column('product_id', Integer, ForeignKey('products.id')),
#     Column('conditional_offer_id', Integer, ForeignKey('conditional_offer.id')),
# )


class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, default=0.0)
    
    # Many to many relation to Conditional offers
    conditional_offers = relationship(
        'ConditionalOffers',
        secondary="products_condition_off_m2m_link",
        overlaps="products",
        back_populates='products'
    )
