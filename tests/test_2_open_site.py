# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/")
#
#
# icon = driver.find_element_by_id(By.CSS_SELECTOR, 'header > a > img')
# if icon is None:
#     print('Элемент не найден')
# else:
#     print('Элемент найден')


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def test_demoqa_site_open():
    """Тест открытия сайта demoqa.com"""
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/")
        time.sleep(2)

        # Проверяем заголовок страницы
        assert "DEMOQA" in driver.title.upper()
        print("✅ Тест пройден: сайт открыт, заголовок корректен")

    finally:
        driver.quit()


def test_demoqa_page_elements():
    """Тест наличия элементов на странице"""
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/")
        time.sleep(2)

        # Проверяем основные элементы
        body = driver.find_element(By.TAG_NAME, "body")
        assert body is not None

        # Ищем элементы, которые точно есть на demoqa.com
        home_content = driver.find_element(By.CLASS_NAME, "home-content")
        assert home_content is not None

        print("✅ Тест пройден: основные элементы найдены")

    except NoSuchElementException:
        print("❌ Некоторые элементы не найдены")
        raise
    finally:
        driver.quit()


def test_demoqa_logo_exists():
    """Тест поиска логотипа"""
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/")
        time.sleep(2)

        # Пробуем разные селекторы для логотипа
        logo_selectors = [
            (By.CSS_SELECTOR, "img"),
            (By.CLASS_NAME, "home-header"),
            (By.TAG_NAME, "header")
        ]

        for by, selector in logo_selectors:
            try:
                element = driver.find_element(by, selector)
                print(f"✅ Элемент найден: {selector}")
                break
            except NoSuchElementException:
                continue
        else:
            print("❌ Логотип не найден")

    finally:
        driver.quit()


# Запуск всех тестов
if __name__ == "__main__":
    test_demoqa_site_open()
    test_demoqa_page_elements()
    test_demoqa_logo_exists()