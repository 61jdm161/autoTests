import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Запуск браузера в headless-режиме (без UI)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_izvozchik_reviews_real_count(driver):
    # Сразу открываем вкладку "Отзывы"
    url = "https://ap-pro.ru/stuff/zov_pripjati/izvozchik-r463/?tab=reviews"
    driver.get(url)

    # Явное ожидание загрузки блока с отзывами (по class="ipsComment_content")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ipsComment_content"))
    )

    # Получаем список всех блоков с отзывами
    comments = driver.find_elements(By.CSS_SELECTOR, "div.ipsComment_content")

    # Проверка: должно быть ровно 7 отзывов
    assert len(comments) == 7, f"Ожидалось 7 отзывов, но найдено: {len(comments)}"


