from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.post("/v1/tokens")
async def get_token():
    return "SECRET_TOKEN"

@app.post("/v1/auth/login")
async def login():
    return "OK"


@app.get("/api/customerAddress")
async def get_customer_address():
    return "221b Baker Street, London"
