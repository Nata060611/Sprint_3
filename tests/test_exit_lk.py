from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators
from helpers import generate_existent_user

class TestExitLK:

    def test_open_lk_and_exit(self, my_chrome):
        existent_user = generate_existent_user()
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/login")
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        my_chrome.find_element(By.XPATH, loc.button_lk_mainpage).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_exit_in_lk)))
        my_chrome.find_element(By.XPATH, loc.button_exit_in_lk).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.h2_enter)))
        button_login = my_chrome.find_element(By.XPATH, loc.button_login_loginpage).text
        assert button_login == "Войти"
