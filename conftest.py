import pytest
from selene import browser
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_managament():

    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'