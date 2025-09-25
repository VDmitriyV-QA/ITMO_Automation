from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def check_saucedemo_elements():
    """
    Функция которая:
    a. переходит на страницу https://www.saucedemo.com/
    b. находит элементы: username, password, submit
    c. Проверяет, если элементы найдены - выводит "Элементы найдены"
    """

    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com/")
        time.sleep(2)


        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")


        if username_field and password_field and submit_button:
            print("Элементы найдены")
            print(f"Поле username: {username_field.get_attribute('placeholder')}")
            print(f"Поле password: {password_field.get_attribute('placeholder')}")
            print(f"Кнопка: {submit_button.get_attribute('value')}")

        return True

    except NoSuchElementException as e:
        print(f"Ошибка: элемент не найден - {e}")
        return False

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

    finally:
        driver.quit()



def check_saucedemo_elements_detailed():
    """Более детальная проверка элементов"""
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        elements_found = True
        elements_info = []


        try:
            username_field = driver.find_element(By.ID, "user-name")
            elements_info.append("✓ Поле username найдено")
        except NoSuchElementException:
            elements_info.append("✗ Поле username не найдено")
            elements_found = False

        try:
            password_field = driver.find_element(By.ID, "password")
            elements_info.append("✓ Поле password найдено")
        except NoSuchElementException:
            elements_info.append("✗ Поле password не найдено")
            elements_found = False

        try:
            submit_button = driver.find_element(By.ID, "login-button")
            elements_info.append("✓ Кнопка submit найдена")
        except NoSuchElementException:
            elements_info.append("✗ Кнопка submit не найдена")
            elements_found = False


        print("\n".join(elements_info))

        if elements_found:
            print("\nЭлементы найдены")
        else:
            print("\nНе все элементы найдены")

        return elements_found

    finally:
        driver.quit()



def test_saucedemo_elements():
    """Тестовая функция для pytest"""
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)


        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")


        assert username_field.is_displayed()
        assert password_field.is_displayed()
        assert submit_button.is_displayed()

        print("Элементы найдены")

    except Exception as e:
        print(f"Ошибка: {e}")
        raise
    finally:
        driver.quit()



if __name__ == "__main__":
    print("=== Проверка элементов на saucedemo.com ===")
    check_saucedemo_elements()

    print("\n=== Детальная проверка ===")
    check_saucedemo_elements_detailed()