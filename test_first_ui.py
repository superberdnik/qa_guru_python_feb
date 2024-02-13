from selene import browser, have, be
import pytest

browser.config.browser_name = 'firefox'

browser.config.hold_browser_open = True


@pytest.fixture()
def size_window():
    browser.config.window_height = 400
    browser.config.window_width = 600
    yield


def test_auth(size_window):
    browser.open('https://qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('qwer@ty.io')
    browser.element('.login-form [name=password]').type('Qwerty123456').press_enter()

    browser.element('.main-header__login').click()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
