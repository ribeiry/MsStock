from fastapi import FastAPI, APIRouter
from mangum import Mangum
from servicesStock import router as book_router
import logging
from dotenv import dotenv_values
from pymongo import MongoClient
import logging

config = dotenv_values(".env")

# SetUp loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root loggers
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome  Stock application !"}


@app.on_event("startup")
def startup_db_client():
    logger.info("logging from the startup_db_client")
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    logger.info("Connected to the MongoDB database !")


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("Shutdown the database connection")
    app.mongodb_client.close()


app.include_router(book_router, tags=["stock"], prefix="/stock")
handler = Mangum(app=app)
