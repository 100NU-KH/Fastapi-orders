from database import Base

import models.products
from sqlalchemy import Enum
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String, ForeignKey, Float

from typing import List
import models
from enums import ConditionalOfferStatus, ConditionType, BenefitType


class Conditions(Base):
    __tablename__ = 'conditions'
    
    description = Column(String, nullable=False)
    typ = Column(String, Enum(ConditionType))
    value = Column(Float)
    
    offer = relationship('ConditionalOffers', back_populates='condition')


class Benefits(Base):
    __tablename__ = 'benefit'
    
    description = Column(String, nullable=False)
    typ = Column(String, Enum(BenefitType))
    value = Column(Float, default=0.0)
    
    offer = relationship('ConditionalOffers', back_populates='benifit')
    

class ConditionalOffers(Base):
    __tablename__ = 'conditional_offer'
    
    name = Column(String, nullable=False, unique=True)
    status = Column(String, Enum(ConditionalOfferStatus))
    condition_id = Column(Integer, ForeignKey('conditions.id'), nullable=True)
    benifit_id = Column(Integer, ForeignKey('benefit.id'), nullable=True)
    
    condition = relationship('Conditions', back_populates='offer')
    
    products = relationship('Products', secondary='products_condition_off_m2m_link', back_populates="conditional_offers")
    
    benifit = relationship('Benefits', back_populates='offer')
    