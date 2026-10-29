from fastapi.testclient import TestClient
from starlette import status

from lanterne.main import app

client = TestClient(app)


def test_health():
    res = client.get("/api/health")
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {"status": "ok"}
