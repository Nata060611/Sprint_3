import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from mydriver import MyChrome
from locators import BurgerLocators
from conftest import *

class TestOpenLK:

    def test_open_lk_and_exit(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/login")
        loc = BurgerLocators()

        # Заполняем email и пароль в форме входа
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(1)

        # Нажимаем на кнопку Вход и для существующего пользователя переходим на главную
        mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()
        WebDriverWait(mychrome.driver, 2)

        # Переходим в профиль авторизованного пользователя и ждем появления кнопки Выход
        mychrome.driver.find_element(By.XPATH, loc.button_lk_mainpage).click()
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_exit_in_lk)))

        time.sleep(1)

        # Кликаем по кнопке Выход
        mychrome.driver.find_element(By.XPATH, loc.button_exit_in_lk).click()

        # Должны перейти настраницу входа
        WebDriverWait(mychrome.driver, 2)

        time.sleep(1)

        current_url = mychrome.driver.current_url

        assert current_url == "https://stellarburgers.nomoreparties.site/login"

        mychrome.driver.quit()

