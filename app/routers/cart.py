from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from typing import List

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=schemas.CartResponse)
def add_to_cart(item: schemas.CartAdd, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    cart_item = models.Cart(user_id=current_user.id, product_id=item.product_id, quantity=item.quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/", response_model=List[schemas.CartResponse])
def get_cart(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Cart).filter(models.Cart.user_id == current_user.id).all()

@router.delete("/{item_id}")
def remove_from_cart(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    item = db.query(models.Cart).filter(models.Cart.id == item_id, models.Cart.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item removed from cart"}