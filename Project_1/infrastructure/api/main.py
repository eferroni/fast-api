import os
from fastapi import FastAPI
from dotenv import load_dotenv

from infrastructure.__shared__.repository.mongo.database import mongo_startup_db_client, mongo_shutdown_db_client
from infrastructure.api.v1.routes import book_route as book_route_v1
from infrastructure.api.v2.routes import (
    user_route as user_route_v2,
    book_route as book_route_v2,
    auth_route as auth_route_v2,
    account_route as account_route_v2
)
from infrastructure.__shared__.constants import repository

app = FastAPI()

# V1
api_v1 = FastAPI()
api_v1.include_router(book_route_v1.router)

# V2
api_v2 = FastAPI()
api_v2.include_router(auth_route_v2.router)
api_v2.include_router(account_route_v2.router)
api_v2.include_router(book_route_v2.router)
api_v2.include_router(user_route_v2.router)

# Mount Versions
app.mount("/v1", api_v1)
app.mount("/v2", api_v2)

# Define start and stop behaviours
load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")


# @app.on_event("startup")
# def startup_db_client():
#     if REPOSITORY == repository.MONGO:
#         mongo_startup_db_client(app)
#
#
# @app.on_event("shutdown")
# def shutdown_db_client():
#     if REPOSITORY == 'mongodb':
#         mongo_shutdown_db_client(app)
