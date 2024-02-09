import pytest
import random


@pytest.fixture
def get_admin(browser, teardown):
    return random.randint(0, 100)


def test_simple(get_admin, browser):
    print(browser)
    # assert get_admin == 5, "айдишник администратора ожидался 5"
    # assert browser == "Chrome"
    assert 1 == 1, "единица не должна быть равна двойке"


def test_another(get_admin, browser):
    assert 1 == 1
    print(browser)
    # assert get_admin == 5, "айдишник администратора ожидался 5"