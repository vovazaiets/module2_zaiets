import schemes, crud
from database import get_db

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

ml_router = APIRouter(prefix="/ml", tags=["records"])

@ml_router.post("/")
def create_model(db: Session = Depends(get_db)):

    return crud.create_model(db)

@ml_router.post("/sim")
def run_sim(db: Session = Depends(get_db), text1=None, text2=None):
    
    return crud.simular_record(db, text1, text2)