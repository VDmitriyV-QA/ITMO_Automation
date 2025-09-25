from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def check_saucedemo_elements():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")

        if username_field and password_field and submit_button:
            print("Элементы найдены")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    check_saucedemo_elements()