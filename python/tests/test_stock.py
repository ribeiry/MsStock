from fastapi.testclient import TestClient
from python.main import app
#from test_app import test_app

client = TestClient(app)

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
    resp = client.get("/stock/{id}}",params="3ea41d21-ca7c-4b65-94c1-80752db47bc8")
    assert resp.status_code == 200
    assert resp.json() == {"_id": "3ea41d21-ca7c-4b65-94c1-80752db47bc8","nome": "Celular Samsung S21","type": "Celular",
                            "qtde": 22,
                            "cost": 3.0,
                            "status": "Disponivel"
                            }

def test_create_product():
    """
        Test create a product in the stock
    :return: id of product created
    """

    resp = client.post("/stock/", headers={},json={"nome": "Macbook Pro M2", "type": "Notebook", "qtde": 22, "cost": 10.000,"status": "Disponivel"})
    assert resp.status_code == 201
