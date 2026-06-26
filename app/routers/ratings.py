from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from typing import List

router = APIRouter(prefix="/ratings", tags=["Ratings"])

@router.post("/", response_model=schemas.RatingResponse)
def add_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if rating.stars < 1 or rating.stars > 5:
        raise HTTPException(status_code=400, detail="Stars must be between 1 and 5")
    new_rating = models.Rating(user_id=current_user.id, **rating.model_dump())
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

@router.get("/", response_model=List[schemas.RatingResponse])
def get_ratings(db: Session = Depends(get_db)):
    return db.query(models.Rating).all()