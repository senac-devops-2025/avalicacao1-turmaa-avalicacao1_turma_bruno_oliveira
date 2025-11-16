from app.main import greet

def test_greet_basic():
    assert greet("DevOps") == "Olá, DevOps!!!!!!"
