from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import users, products, cart, orders, ratings, contacts, auth

app = FastAPI(title="StrathMart API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(ratings.router)
app.include_router(contacts.router)

@app.get("/")
def root():
    return {"message": "Welcome to StrathMart!"}