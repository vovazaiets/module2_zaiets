import schemes, crud
from database import get_db
# from app import schemes, crud
# from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

users_router = APIRouter(prefix="/users", tags=["users"])

#"http//:localhost:8000/users"

    
@users_router.post("/", response_model=schemes.User)
def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail=f"User with email={user.email} already exists")

    db_user = crud.create_user(db, user=user)
    return db_user


@users_router.get("/{id}", response_model=schemes.User)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id)
    return db_user

@users_router.get("/get/", )
def get_users(db: Session = Depends(get_db)):
    db_user = crud.get_users(db)
    return db_user

@users_router.put('/{id}', response_model=schemes.User)
def update_user(id: int = None , user: schemes.UserCreate = None, db: Session = Depends(get_db)):
    db_user = crud.update_user( user, db, id)
    return db_user

@users_router.delete('/{id}', response_model=schemes.User)
def delete_user(id: int = None , db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, id)
    return db_user


