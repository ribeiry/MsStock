import logging
from typing import List
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from service.servicesStock import ServiceStock
from model.model import Product

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

router = APIRouter()
servico_estoque = ServiceStock()


@router.post("/", response_description="Create a new product", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    logger.info("create product method")
    pr = jsonable_encoder(product)
    logger.info('routes.py.create_package')
    logger.info(pr)
    create_product = servico_estoque.create_product(pr)
    return create_product


@router.get("/", response_description="List all products of the Stock", status_code=status.HTTP_200_OK, response_model=List[Product])
async def list_products():
    logger.info('routes.py.list_products')
    products = servico_estoque.list_allproducts()
    return products


@router.get("/{id}", response_description="Get an Product in the Stock", status_code=status.HTTP_200_OK, response_model=Product)
async def list_a_product(id: str):
    logger.info('routes.py.list_a_product.id' + id)
    product = servico_estoque.find_product_byid(id)
    if product != "":
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")


@router.put("/{id}/sub", response_description="Take a Product a Stock", status_code=status.HTTP_200_OK, response_model=Product)
async def update_stock(id: str, request: Request):
    qtde = int(request.headers.get('x-qtde'))
    logger.info('routes.py.update_stock.id' + id)
    new_qtde = servico_estoque.take_product(id, qtde)
    if (new_qtde != 0) is not None:
        return new_qtde
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with {id} not found")


@router.put("/{id}/add", response_description="Return a Product a Stock", status_code=status.HTTP_200_OK, response_model=Product)
async def add_stock(id: str, request: Request):
    qtde = int(request.headers.get('x-qtde'))
    logger.info(qtde)
    product_stock = servico_estoque.return_product(id, qtde)
    logger.info('product add in the stock')
    if product_stock != "error":
        return product_stock
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID not found")
