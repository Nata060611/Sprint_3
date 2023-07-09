import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from mydriver import MyChrome
from locators import BurgerLocators
from conftest import *

class TestOpenLK:

    def test_open_lk_authorized_user(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/login")
        loc = BurgerLocators()

        # Заполняем email и пароль в форме входа
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(2)

        # Нажимаем на кнопку Вход и для существующего пользователя переходим на главную
        registration = mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()
        WebDriverWait(mychrome.driver, 2)

        # Переходим в профиль авторизованного пользователя
        mychrome.driver.find_element(By.XPATH, loc.button_lk_mainpage).click()
        WebDriverWait(mychrome.driver, 2)

        time.sleep(2)

        current_url = mychrome.driver.current_url

        assert current_url == "https://stellarburgers.nomoreparties.site/account/profile"

        mychrome.driver.quit()

