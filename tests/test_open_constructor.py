from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators

class TestOpenConstructor:

    def test_open_lk_click_constructor(self, existent_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/login")
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        my_chrome.find_element(By.XPATH, loc.button_lk_mainpage).click()

        WebDriverWait(my_chrome, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        my_chrome.find_element(By.XPATH, loc.a_constructor).click()

        WebDriverWait(my_chrome, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = my_chrome.find_element(By.XPATH, loc.button_order)
        assert 'Оформить заказ' in button.text


