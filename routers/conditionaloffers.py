from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db
from schemas.conditionaloffers import CreateCondition, ConditionsDetails, CreateConditionalOffer, ConditionalOfferDetail
from models import Conditions, ConditionalOffers

router = APIRouter(
    prefix='/offer',
    tags=['Offers']
)

########## CONDITION ROUTES ################
@router.post('/', response_model=ConditionsDetails)
def create_condition(request: CreateCondition, db: Session = Depends(get_db)):
    condition_obj = Conditions(
        description=request.description,
        typ=request.typ.value,
        value=request.value
    )
    db.add(condition_obj)
    db.commit()
    db.refresh(condition_obj)
    return condition_obj


@router.get('/', response_model=List[ConditionsDetails])
def get_all_conditions(db: Session = Depends(get_db)):
    conditions_objs = db.query(Conditions).filter(Conditions.is_active==True).all()
    return conditions_objs

########## CONDITIONAL OFFER ROUTES ################
@router.post('/conditional-offer', response_model=ConditionalOfferDetail)
def create_conditional_offer(request: CreateConditionalOffer, db: Session = Depends(get_db)):
    cond_offr = ConditionalOffers(
        name=request.name,
        status=request.status,
        condition_id=request.condition_id,
        benifit_id=request.benifit_id
    )
    db.add(cond_offr)
    db.commit()
    db.refresh(cond_offr)
    return cond_offr