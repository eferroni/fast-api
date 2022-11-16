from fastapi import FastAPI
from infrastructure.api.v1.routes import book_route as book_route_v1
from infrastructure.api.v2.routes import (
    user_route as user_route_v2,
    book_route as book_route_v2,
    auth_route as auth_route_v2,
    account_route as account_route_v2
)

app = FastAPI()

api_v1 = FastAPI()
api_v1.include_router(book_route_v1.router)

api_v2 = FastAPI()
api_v2.include_router(auth_route_v2.router)
api_v2.include_router(account_route_v2.router)
api_v2.include_router(book_route_v2.router)
api_v2.include_router(user_route_v2.router)

app.mount("/v1", api_v1)
app.mount("/v2", api_v2)
