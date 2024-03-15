import pytest
from selene import browser, be, have, config


@pytest.fixture(scope='session')
def browser_set():
    config.browser_name = 'firefox'
    config.hold_browser_open = True
    config.window_width = 800
    config.window_height = 600
    yield


def test_search_positive(browser_set):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_negative(browser_set):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hweugiuwyebgu').press_enter()
    browser.element('[aria-level="3"]').should(have.text('не найдено'))
