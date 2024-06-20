from fastapi import FastAPI
from pymongo import MongoClient
from test_config import test_config

test_app = FastAPI()


@test_app.on_event("startup")
def startup_test_db_client():
    test_app.mongodb_client = MongoClient(test_config["DB_URI"])
    test_app.database = test_app.mongodb_client[test_config["DB_NAME"]]
