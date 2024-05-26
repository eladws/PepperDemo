from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.post("/app-bff/graphql/query/getCreditLoanStatus")
async def get_credit_loan_status():
    return "OK"


@app.post("/kong/app-bff/graphql/mutation/updateCustomerData")
async def update_customer_data():
    return "Customer data updated!"


@app.get("/v1/balance")
async def get_balance():
    return "100"


@app.get("/v1/customers/{customerId}")
async def get_customer_by_id():
    return {"name": "Sherlock",
            "address": "221b Baker Street, London"}


@app.get("/v1/payments/{paymentId}")
async def get_payment_by_id():
    return {"type": "deposit",
            "amount": 1000000}


@app.get("/v1/tokens")
async def get_token():
    return {"SECRET_TOKEN"}


@app.get("/v1/tokens/{tokenId}")
async def get_token():
    return {"SECRET_TOKEN_ID"}


@app.get("/v2/phone/search")
async def phone_search(phone):
    return get_user_from_db_by_phone(phone)
