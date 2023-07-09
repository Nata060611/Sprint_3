import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from mydriver import MyChrome
from locators import BurgerLocators
from conftest import *

class TestRegistration:

    def test_enter_new_account_created_account(self, newuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/register")
        loc = BurgerLocators()

        # Заполняем имя, email и пароль в форме регистрации
        name = mychrome.driver.find_element(By.XPATH, loc.input_name).send_keys(newuser['name'])
        email = mychrome.driver.find_element(By.XPATH, loc.input_email).send_keys(newuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.input_pass).send_keys(newuser['passw'])

        time.sleep(2)

        # Нажимаем на кнопку Регистрация
        registration = mychrome.driver.find_element(By.XPATH,loc.button_reg).click()

        # Ожидаем, пока произойдет переход на следующую страницу
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.h2_enter)))

        current_url = mychrome.driver.current_url

        assert current_url == "https://stellarburgers.nomoreparties.site/login"

        mychrome.driver.quit()


    def test_enter_new_account_passw_less_6_letters(self, invaliduser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/register")
        loc = BurgerLocators()

        # Заполняем имя, email и неверным пароль в форме регистрации
        name = mychrome.driver.find_element(By.XPATH, loc.input_name).send_keys(invaliduser['name'])
        email = mychrome.driver.find_element(By.XPATH, loc.input_email).send_keys(invaliduser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.input_pass).send_keys(invaliduser['passw'])

        time.sleep(2)

        # Нажимаем на кнопку Регистрация
        registration = mychrome.driver.find_element(By.XPATH,loc.button_reg).click()

        # Ожидаем сообщение об ошибке
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.p_text)))

        error_message = mychrome.driver.find_element(By.XPATH, loc.p_text)

        assert error_message.text == "Некорректный пароль", "НЕВЕРНОЕ УВЕДОМЛЕНИЕ О ТОМ, ЧТО ПАРОЛЬ МЕНЕЕ 6 СИМВОЛОВ"

        mychrome.driver.quit()


