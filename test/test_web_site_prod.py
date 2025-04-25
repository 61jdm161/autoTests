import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_open_s6(brws):
    brws.get('https://demoblaze.com/index.html')
    gS6 = brws.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    gS6.click()
    title = brws.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monik(brws):
    brws.get('https://demoblaze.com/index.html')
    monik_link = brws.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monik_link.click()
    time.sleep(4)
    moniki = brws.find_elements(By.CSS_SELECTOR, '.card')
    print(len(moniki))
    assert len(moniki) == 2


