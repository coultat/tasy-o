from fastapi.testclient import TestClient
from tasy_o.api.app import fastapi_app

client = TestClient(fastapi_app)
