from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root():
    """
        Test an endpoint root of package manager
    """
    resp = client.get("/")
    assert resp.status_code == 200
   # assert resp.json() == {"message":"Welcome  Stock application !"}
