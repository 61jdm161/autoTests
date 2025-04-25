import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def brws():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser