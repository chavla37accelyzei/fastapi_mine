from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app instance is named 'app'

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# dependency testing
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

def get_mock_dependency():
    return "Mocked Dependency"

@app.get("/")
def read_root(dependency: str = Depends(get_mock_dependency)):
    return {"Hello": dependency}

client = TestClient(app)

def test_read_root_with_mock_dependency():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Mocked Dependency"}

    

# debugging
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

 