from fastapi import FastAPI
from infrastructure.api.routes import book_route

app = FastAPI()

app.include_router(book_route.router)
