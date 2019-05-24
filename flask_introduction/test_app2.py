from run_app2 import app
import pytest

@pytest.fixture(scope="module")
def app2():
    app2=app
    app2=app2.test_client()
    app2.testing=True
    print("--------setup--------")
    yield app2
    print("-------teardown--------")

def test_root(app2):
    result=app2.get("/")
    print(result.data[1:5])
    assert result.data[1:4]==b"html"

