from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import users, products, cart, orders, ratings, contacts, auth

app = FastAPI(title="StrathMart API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://strathmart-su.netlify.app",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "null"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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