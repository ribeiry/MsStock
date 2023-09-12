import logging
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values

logger = logging.getLogger(__name__)
config = dotenv_values(".env")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
app = FastAPI()

class Database:

    def __int__(self):
        self = self
    @app.on_event("shutdown")
    def shutdown_db_client(self):
        logger.info("Shutdown the database connection")
        app.mongodb_client.close()

    def startup_db_client(self):
        logger.info("logging from the startup_db_client")
        client = MongoClient(config["DB_URI"])
        database = client[config["DB_NAME"]]
        logger.info("Connected to the MongoDB database !")
        return database
