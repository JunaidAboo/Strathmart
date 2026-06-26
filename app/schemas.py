from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

# --- Enums ---
class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    delivered = "delivered"
    cancelled = "cancelled"

class ContactStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"

# --- User Schemas ---
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True

# --- Category Schemas ---
class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# --- Product Schemas ---
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image_url: Optional[str] = None
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int
    image_url: Optional[str]
    is_available: bool
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- Cart Schemas ---
class CartAdd(BaseModel):
    product_id: int
    quantity: int = 1

class CartResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    added_at: datetime

    class Config:
        from_attributes = True

# --- Order Schemas ---
class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price_at_purchase: float

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    status: OrderStatus
    total_price: float
    created_at: datetime
    items: list[OrderItemResponse]

    class Config:
        from_attributes = True

# --- Rating Schemas ---
class RatingCreate(BaseModel):
    stars: int
    comment: Optional[str] = None

class RatingResponse(BaseModel):
    id: int
    stars: int
    comment: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

# --- Contact Schemas ---
class ContactCreate(BaseModel):
    subject: str
    message: str

class ContactResponse(BaseModel):
    id: int
    subject: str
    message: str
    status: ContactStatus
    created_at: datetime

    class Config:
        from_attributes = True