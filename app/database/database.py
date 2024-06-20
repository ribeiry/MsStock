import logging

from fastapi import FastAPI
from pymongo import MongoClient

from app.utils.logger import Logger
from app.utils.setting import Settings


class Database:

    def __int__(self):
        self.__logger = Logger(__name__)
        self.__settings = Settings.get_settings()

    @app.on_event("shutdown")
    def shutdown_db_client(self):
        self.__logger.info("Shutdown the database connection")
        app.mongodb_client.close()

    def startup_db_client(self):
        self.__logger.info("logging from the startup_db_client")
        client = MongoClient(host=self.__settings.db_uri)
        database = client[self.__settings.db_name]
        self.__logger.info("Connected to the MongoDB database !")
        return database
