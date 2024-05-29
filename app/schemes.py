from pydantic import BaseModel

from datetime import date


class ModelCreate(BaseModel):
    pass

class SimilarityText(BaseModel):
    text1: str
    text2: str


class RecordBase(BaseModel):
    date: date
    title: str
    content: str
    
    class Config:
        orm_mode = True


class RecordCreate(RecordBase):
    user_id: int
    title: str
    content: str

class UsersGetAll(BaseModel):
    pass

class Record(RecordBase):
    id: int
    user_id: int
    date: date


class UserBase(BaseModel):
    first_name: str
    second_name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    records: list[Record] = []

    class Config:
        orm_mode = True

class RecordUpdate(RecordBase):
    id: int
