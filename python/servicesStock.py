import json
import uuid

from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import logging
from model import Product, StockUpdate

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_description="Create a new product", status_code=status.HTTP_201_CREATED)
def create_product(request: Request, product: Product):
    logger.info("create product method")
    pr = jsonable_encoder(product)
    logger.info('routes.py.create_package')
    logger.info(pr)
    new_package = request.app.database["stock"].insert_one(pr)
    created_product = request.app.database["stock"].find_one(
        {"_id": new_package.inserted_id}
    )
    logger.info('The package id is')

    return created_product


@router.get("/", response_description="List all products of the Stock", response_model=List[Product])
def list_products(resquest: Request):
    products = list(resquest.app.database["stock"].find(limit=1000))
    logger.info('routes.py.list_products')
    return products


@router.get("/{id}", response_description="Get an Product in the Stock", response_model=Product)
def list_a_product(id: str, request: Request):
    logger.info('routes.py.list_a_product.id' + id)
    if (product := request.app.database["stock"].find_one({"_id": id})) is not None:
        logger.info('routes.py.list_a_product.id' + id)
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")


@router.put("/{id}/sub", response_description="Take a Product a Stock", response_model=Product)
def update_stock(id: str, request: Request):
    qtde = int(request.headers.get('x-qtde'))
    global qtde_product
    logger.info('routes.py.update_stock.id' + id)
    if product := request.app.database["stock"].find_one({"_id": id}):
        logger.info('routes.py.update_stock')
        qtde_product = product["qtde"]
    if qtde >= 1:
        if qtde_product >= qtde:
            product["qtde"] = qtde_product - qtde
        else:
            product["qtde"] -= qtde_product
            product["status"] = "indisponivel"
        logger.info(product)
        update_result = request.app.database["stock"].update_one(
            {"_id": id},{"$set": product}
        )
        logger.info(update_result)
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID not found")

    if (new_qtde := request.app.database["stock"].find_one({"_id": id})) is not None:
            logger.info(new_qtde)
            return new_qtde
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with {id} not found")


@router.put("/{id}/add", response_description="Return a Product a Stock", response_model=Product)
def add_stock(id: str, request: Request):
    qtde = int(request.headers.get('x-qtde'))
    logger.info(qtde)
    global qtde_product
    logger.info('routes.py.update_stock.id' + id)
    if product := request.app.database["stock"].find_one({"_id": id}):
        logger.info('routes.py.update_stock')
        qtde_product = product["qtde"]
    if qtde >= 1:
        product["qtde"] = qtde_product + qtde

        logger.info(product)
        update_result = request.app.database["stock"].update_one(
            {"_id": id},{"$set": product}
        )
        logger.info(update_result)
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID not found")

    if (new_qtde := request.app.database["stock"].find_one({"_id": id})) is not None:
            logger.info(new_qtde)
            return new_qtde
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with {id} not found")

