from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators

class TestRegistration:

    def test_enter_new_account_created_account(self, new_user, my_chrome):
        my_chrome.get("https://stellarburgers.nomoreparties.site/register")
        loc = BurgerLocators()

        my_chrome.find_element(By.XPATH, loc.input_name_reg_page).send_keys(new_user['name'])
        my_chrome.find_element(By.XPATH, loc.input_email_reg_page).send_keys(new_user['email'])
        my_chrome.find_element(By.XPATH, loc.input_pass_reg_page).send_keys(new_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_reg).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.h2_enter)))
        current_url = my_chrome.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/login"



    def test_enter_new_account_passw_less_6_letters(self, invalid_user, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site/register")

        my_chrome.find_element(By.XPATH, loc.input_name_reg_page).send_keys(invalid_user['name'])
        my_chrome.find_element(By.XPATH, loc.input_email_reg_page).send_keys(invalid_user['email'])
        my_chrome.find_element(By.XPATH, loc.input_pass_reg_page).send_keys(invalid_user['passw'])
        my_chrome.find_element(By.XPATH,loc.button_reg).click()

        WebDriverWait(my_chrome, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.p_error_pass)))
        error_message = my_chrome.find_element(By.XPATH, loc.p_error_pass)
        assert error_message.text == "Некорректный пароль", "НЕВЕРНОЕ УВЕДОМЛЕНИЕ О ТОМ, ЧТО ПАРОЛЬ МЕНЕЕ 6 СИМВОЛОВ"
