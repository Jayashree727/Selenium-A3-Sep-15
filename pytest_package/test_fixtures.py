import pytest

@pytest.fixture()
def greet():
    print("good morning")

def test_login(greet):
    print("login executing")

def test_logout(greet):
    print("logout executing")

