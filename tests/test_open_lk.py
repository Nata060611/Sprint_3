from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators
from helpers import generate_existent_user

class TestOpenLK:

    def test_open_lk_authorized_user(self, my_chrome):
        existent_user = generate_existent_user()
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/login")
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        my_chrome.find_element(By.XPATH, loc.button_lk_mainpage).click()

        WebDriverWait(my_chrome, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        current_url = my_chrome.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/account/profile"


