from fastapi import FastAPI
from mangum import Mangum
from controller.StockController import router as book_router
from dotenv import dotenv_values
from pymongo import MongoClient
import logging



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# get root loggers
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome  Stock application !"}


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("Shutdown the database connection")
    app.mongodb_client.close()


app.include_router(book_router, tags=["stock"], prefix="/stock")
handler = Mangum(app=app)
