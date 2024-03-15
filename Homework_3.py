from selene import browser, config, be, have
import pytest

# config.browser_name = "Firefox"


@pytest.fixture()
def browser_set():
    browser.open("https://demoqa.com/automation-practice-form")
    yield


browser.element('[id=firstname]').
browser.element('id=lastname')
browser.element('id=useremail')

