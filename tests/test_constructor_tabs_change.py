from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocators

class TestConstructorTabs:

    def test_open_constructor_tap_second(self, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site")
        my_chrome.find_element(By.XPATH, loc.tabs_souses).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.tabs_souses_h2)))
        active_tab = my_chrome.find_element(By.XPATH, loc.tabs_current)
        assert active_tab.text == "Соусы"


    def test_open_constructor_tap_third(self, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site")
        my_chrome.find_element(By.XPATH, loc.tabs_nachinki).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.tabs_nachinki_h2)))
        active_tab = my_chrome.find_element(By.XPATH, loc.tabs_current)
        assert active_tab.text == "Начинки"


    def test_open_constructor_tap_third_then_first(self, my_chrome):
        loc = BurgerLocators()
        my_chrome.get("https://stellarburgers.nomoreparties.site")
        my_chrome.find_element(By.XPATH, loc.tabs_nachinki).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.tabs_nachinki_h2)))
        my_chrome.find_element(By.XPATH, loc.tabs_bulki).click()

        WebDriverWait(my_chrome, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, loc.tabs_bulki_h2)))
        active_tab = my_chrome.find_element(By.XPATH, loc.tabs_current)
        assert active_tab.text == "Булки"
