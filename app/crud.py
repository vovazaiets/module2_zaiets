from typing import Union, Optional

# from app import models
# from app import schemes
import models
import schemes
from sqlalchemy.orm import Session
from sqlalchemy import select
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from models import Record
nltk.download('punkt')
nltk.download('stopwords')


def preprocess(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens



def create_model(db: Session):

    texts = db.execute(select(Record.content)).all()
    corpus = [preprocess(str(text)) for text in texts]
    w2v_model = Word2Vec(corpus, vector_size=100, window=5, min_count=1, workers=4, epochs=10)
    w2v_model.save('trained_model.model')

    return 'Trained'

def simular_record(db: Session, t1, t2):

    model = Word2Vec.load('trained_model.model')

    return f"{model.wv.similarity(t1, t2)}"


#USER
def create_user(db: Session, user: schemes.UserCreate) -> schemes.User:
    db_user = models.User(email=user.email, first_name=user.first_name,
                          second_name=user.second_name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, id: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def update_user(user: schemes.UserCreate, db: Session, id: int) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.id == id).first()
    db_user.email=user.email
    db_user.first_name=user.first_name
    db_user.second_name=user.second_name
    db_user.password=user.password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: str) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.id==id).delete()
    db.commit()
    return db_user
    

#RECORDS
def create_record(db: Session, record = models.Record) -> schemes.Record:
    db_record = models.Record(date=record.date, title=record.title, content=record.content, user_id=record.user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session):
    return db.query(models.Record).all()

def get_record_by_id(db: Session, id: str) -> Optional[models.Record]:
    return db.query(models.Record).filter(models.Record.id == id).first()

def update_record(db: Session, record: schemes.RecordUpdate, id: int) -> Optional[models.Record]:
    db_record = db.query(models.Record).filter(models.Record.id == id).first()
    db_record.title=record.title
    db_record.content=record.content
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def delete_record(db: Session, id: str) -> Optional[models.Record]:
    db_record = db.query(models.Record).filter(models.Record.id==id).delete()
    db.commit()
    return db_record