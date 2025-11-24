import pytest

@pytest.mark.dependency()
def test_login():
    raise Exception

@pytest.mark.dependency()
def test_reg():
    print("reg executing")


@pytest.mark.dependency(depends=['test_login', test_reg])
def test_logout():
    print("logout executing")