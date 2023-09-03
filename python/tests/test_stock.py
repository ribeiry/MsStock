from fastapi.testclient import TestClient
from python.main import app

client = TestClient(app)


def test_root():
    """
        Test an endpoint root of package manager
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome  Stock application !"}


def test_create_product():
    """
        Test create a product in the stock
    :return: id of product created
    """

    resp = client.post("/stock", json={"nome": "Macbook Pro M2", "type": "Notebook", "qtde": 22, "cost": 10.000,
                                       "status": "Disponivel"})
    assert resp.status_code == 201
