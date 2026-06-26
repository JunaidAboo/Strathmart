from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from typing import List, Optional

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/", response_model=schemas.ContactResponse)
def submit_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db), current_user: Optional[models.User] = Depends(get_current_user)):
    new_contact = models.Contact(user_id=current_user.id if current_user else None, **contact.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@router.get("/", response_model=List[schemas.ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    return db.query(models.Contact).all()