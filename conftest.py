import pytest
from selenium import webdriver

@pytest.fixture()
def brws():

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser