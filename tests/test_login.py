from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators

class TestLogin:

    def test_main_page_login(self, existent_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site")
        my_chrome.find_element(By.XPATH, loc.button_login_mainpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = my_chrome.find_element(By.XPATH,loc.button_order)
        assert 'Оформить заказ' in button.text


    def test_main_page_LK(self, existent_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site")
        my_chrome.find_element(By.XPATH, loc.button_lk_mainpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = my_chrome.find_element(By.XPATH,loc.button_order)
        assert 'Оформить заказ' in button.text


    def test_login_from_registration_page(self, existent_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/register")
        my_chrome.find_element(By.XPATH, loc.button_login_reg_and_recover_page).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = my_chrome.find_element(By.XPATH,loc.button_order)
        assert 'Оформить заказ' in button.text


    def test_login_from_recover_page(self, existent_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/forgot-password")
        my_chrome.find_element(By.XPATH, loc.button_login_reg_and_recover_page).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_login_loginpage)))
        my_chrome.find_element(By.XPATH, loc.login_input_email).send_keys(existent_user['email'])
        my_chrome.find_element(By.XPATH, loc.login_input_pass).send_keys(existent_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_login_loginpage).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.button_order)))
        button = my_chrome.find_element(By.XPATH,loc.button_order)
        assert 'Оформить заказ' in button.text
