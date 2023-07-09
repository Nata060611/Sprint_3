import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from mydriver import MyChrome
from locators import BurgerLocators
from conftest import *

class TestLogin:

    def test_main_page_login(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        # Переходим с главной страницы на страницу логина
        mychrome.driver.find_element(By.XPATH, loc.button_login_mainpage).click()
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))

        # Заполняем email и пароль, нажимаем "Войти"
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(1)
        mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()

        # Ждем появления кнопки "Оформить заказ"
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = mychrome.driver.find_element(By.XPATH,loc.button_order)

        time.sleep(1)

        # Проверь, что на странице есть кнопка, с текстом 'Оформить заказ'
        assert 'Оформить заказ' in button.text

        mychrome.driver.quit()


    def test_main_page_LK(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        # Переходим с главной страницы на страницу логина через кнопку Личный кабинет
        mychrome.driver.find_element(By.XPATH, loc.button_lk_mainpage).click()
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))

        # Заполняем email и пароль, нажимаем "Войти"
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(1)
        mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()

        # Ждем появления кнопки "Оформить заказ"
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = mychrome.driver.find_element(By.XPATH,loc.button_order)

        time.sleep(1)

        # Проверь, что на странице есть кнопка, с текстом 'Оформить заказ'
        assert 'Оформить заказ' in button.text

        mychrome.driver.quit()


    def test_login_from_registration_page(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/register")
        loc = BurgerLocators()
        time.sleep(1)

        # Переходим с со страницы регистрации на страницу логина
        mychrome.driver.find_element(By.XPATH, loc.button_login_reg_and_recover_page).click()
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))

        # Заполняем email и пароль, нажимаем "Войти"
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(1)
        mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()

        # Ждем появления кнопки "Оформить заказ"
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = mychrome.driver.find_element(By.XPATH,loc.button_order)

        time.sleep(1)

        # Проверь, что на странице есть кнопка, с текстом 'Оформить заказ'
        assert 'Оформить заказ' in button.text

        mychrome.driver.quit()


    def test_login_from_recover_page(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site/forgot-password")
        loc = BurgerLocators()
        time.sleep(1)

        # Переходим с со страницы восстановления пароля на страницу логина
        mychrome.driver.find_element(By.XPATH, loc.button_login_reg_and_recover_page).click()
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))

        # Заполняем email и пароль, нажимаем "Войти"
        email = mychrome.driver.find_element(By.XPATH, loc.login_input_email).send_keys(existentuser['email'])
        password = mychrome.driver.find_element(By.XPATH, loc.login_input_pass).send_keys(existentuser['passw'])
        time.sleep(1)
        mychrome.driver.find_element(By.XPATH,loc.button_login_loginpage).click()

        # Ждем появления кнопки "Оформить заказ"
        WebDriverWait(mychrome.driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = mychrome.driver.find_element(By.XPATH,loc.button_order)

        time.sleep(1)

        # Проверь, что на странице есть кнопка, с текстом 'Оформить заказ'
        assert 'Оформить заказ' in button.text

        mychrome.driver.quit()


