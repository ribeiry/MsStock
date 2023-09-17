import sqlite3
from python.database.DatabaseMock import DatabaseMock
import pytest
from fastapi.testclient import TestClient
from python.main import app
from model.model import Product

client = TestClient(app)
@pytest.fixture # 1
def session():
    connection = sqlite3.connect(':memory:') # 2
    db_session = connection.cursor()
    yield db_session# 5
    connection.close()

@pytest.fixture
def setup_db(session):
    session.execute('''CREATE TABLE Product
                             (_id uuid, nome string,type string, qtde int, cost float,status string)''')  # 3
    session.execute(
        'INSERT INTO Product VALUES ("066de609-b04a-4b30-b46c-32537c7f1fja","Macbook Pro M2","Notebook",22,10.000,"Disponivel")')  # 4
    session.connection.commit()

DatabaseMock = DatabaseMock(DatabaseMock)
@pytest.fixture
def cache(session): # 1
    return

def test_root():
    """
        Test an endpoint root of package manager
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome  Stock application !"}


def test_get_product():
    """
        Test get a product for an id
    :return: a product
    """
    id = "066de609-b04a-4b30-b46c-32537c7f1f6e"
    resp = client.get(f"/stock/{id}")
    assert resp.status_code == 200


@pytest.mark.usefixtures("setup_db")
def test_get_all_product(session):
    """
        Test get a product for an id
    :return: a product
    """
    DatabaseMock.__init__(session)

    if DatabaseMock is not None:
        existing = DatabaseMock.get_product("066de609-b04a-4b30-b46c-32537c7f1fja")
        assert existing


@pytest.mark.usefixtures("setup_db")
def test_create_product(session):
    """
        Test create a product in the stock
    :return: id of product created
    """
    DatabaseMock.__init__(session)
    Product.id     = "066de609-b04a-4b30-b46c-32537c7f1f6e"
    Product.nome   = "Samsung TV 53"
    Product.type   = "TV"
    Product.qtde   = "2"
    Product.cost   = "2500.00"
    Product.status = "Disponivel"
    if DatabaseMock is not None:
        DatabaseMock.save_status(Product)
        existing = DatabaseMock.get_product(Product.id)
        assert existing

