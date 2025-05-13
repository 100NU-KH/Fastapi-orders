from typing import List
from fastapi import APIRouter, Depends
from database import get_db

from models import Benefits
from schemas.benefits import CreateBenefit, BenefitDetails
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/benefit',
    tags=['Benefits']
)


@router.post('/', response_model=BenefitDetails)
def create_benefit(request: CreateBenefit, db: Session = Depends(get_db)):
    new_benefit = Benefits(
        description=request.description,
        typ=request.typ.value,
        value=request.value
    )
    db.add(new_benefit)
    db.commit()
    db.refresh(new_benefit)
    return new_benefit

@router.get('/', response_model=List[BenefitDetails])
def get_all_benefits(db: Session = Depends(get_db)):
    benefits = db.query(Benefits).filter(Benefits.is_active==True).all()
    return benefits