import pytest

@pytest.fixture
def teardown():
    yield
    print("do sth")


@pytest.fixture(scope="session")
def browser():
    print("открываем браузер")
    yield random.randint(0, 100)
    print("закрываем браузер")
