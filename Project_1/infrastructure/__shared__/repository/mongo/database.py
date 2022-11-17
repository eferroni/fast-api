import os

import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get("MONGO_URL")
DB_NAME = os.environ.get("MONGO_DB_NAME")


def get_database():
    client = MongoClient(DB_URL, tlsCAFile=certifi.where())
    return client[DB_NAME]


def mongo_startup_db_client(app):
    app.mongodb_client = MongoClient(DB_URL)
    app.database = app.mongodb_client[DB_NAME]
    print("Connected to the MongoDB database!")


def mongo_shutdown_db_client(app):
    app.mongodb_client.close()
