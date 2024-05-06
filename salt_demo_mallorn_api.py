from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/auth")
async def auth():
    return get_user_auth()


@app.get("/api/cart")
async def cart():
    return get_user_cart()

@app.get("/api/customerAddress")
async def get_customer_address():
    return "221b Baker Street, London"


@app.get("/api/user/{userId}")
async def get_user_by_id():
    return get_user(id="uesrId")
