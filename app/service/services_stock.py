from database.database import Database
from fastapi import FastAPI
from model.model import Product

from app.utils.logger import Logger

app = FastAPI()
db = Database()


class ServiceStock:

    def __int__(self):
        self.__logger = Logger(__name__)

    def create_product(self, product: Product):
        new_package = db.startup_db_client()["stock"].insert_one(product)
        created_product = self.find_product_byid(new_package.inserted_id)
        self.__logger.info("The package id is")

        return created_product

    def list_allproducts(self):
        products = list(db.startup_db_client()["stock"].find(limit=1000))
        self.__logger.info("routes.py.list_products")
        return products

    def find_product_byid(self, id: str):
        self.__logger.info("servicestock.py.find_product_byid" + id)
        if (product := db.startup_db_client()["stock"].find_one({"_id": id})) is not None:
            self.__logger.info("routes.py.list_a_product.id" + id)
            return product
        return ""

    def take_product(self, id: str, qtde: int):
        global qtde_product
        if product := self.find_product_byid(id):
            self.__logger.info("routes.py.update_stock")
            qtde_product = product["qtde"]
        if qtde >= 1:
            if qtde_product >= qtde:
                product["qtde"] = qtde_product - qtde
            else:
                product["qtde"] -= qtde_product
                product["status"] = "Indisponivel"
            self.__logger.info(product)

            update_result = db.startup_db_client()["stock"].update_one({"_id": id}, {"$set": product})
            self.__logger.info(update_result)
        if (new_qtde := self.find_product_byid(id)) is not None:
            self.__logger.info(new_qtde)
            return new_qtde
        return 0

    def return_product(self, id: str, qtde: int):
        global qtde_product
        self.__logger.info("routes.py.update_stock.id" + id)
        if product := self.find_product_byid(id):
            self.__logger.info("routes.py.update_stock")
            qtde_product = product["qtde"]
        if qtde >= 1:
            product["qtde"] = qtde_product + qtde
            product["status"] = "Disponivel"
            self.__logger.info(product)
            db.startup_db_client()["stock"].update_one({"_id": id}, {"$set": product})
            update_result = self.find_product_byid(id)
            return update_result
        return "error"
