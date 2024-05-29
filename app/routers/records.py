# from app import schemes, crud
# from app.database import get_db
import schemes, crud
from database import get_db

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

records_router = APIRouter(prefix="/records", tags=["records"])


@records_router.post("/", response_model=schemes.Record)
def create_record(record: schemes.RecordCreate, db: Session = Depends(get_db)):
    db_record = crud.create_record(db, record )
    return db_record

@records_router.get("/get/", )
def get_records(db: Session = Depends(get_db)):
    db_record = crud.get_records(db)
    return db_record

@records_router.get("/{id}", response_model=schemes.Record)
def get_record(id: int, db: Session = Depends(get_db)):
    db_record = crud.get_record_by_id(db, id=id)
    return db_record 

@records_router.put('/{id}', response_model=schemes.Record)
def update_record(id: int = None , record: schemes.RecordUpdate = None, db: Session = Depends(get_db)):
    db_record = crud.update_record( db, record,  id)
    return db_record

@records_router.delete('/{id}', response_model=schemes.Record)
def delete_record(id: int = None , db: Session = Depends(get_db)):
    db_record = crud.delete_record(db, id)
    return db_record
