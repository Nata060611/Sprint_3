import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from mydriver import MyChrome
from locators import BurgerLocators
from conftest import *

class TestOpenLK:

    def test_open_constructor_first_active(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        time.sleep(1)

        active_tab = mychrome.driver.find_element(By.XPATH, loc.div_current)

        assert active_tab.text == "Булки"

        mychrome.driver.quit()

    def test_open_constructor_tap_second(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        time.sleep(1)

        mychrome.driver.find_element(By.XPATH, loc.div_second).click()

        time.sleep(1)

        active_tab = mychrome.driver.find_element(By.XPATH, loc.div_current)

        assert active_tab.text == "Соусы"

        mychrome.driver.quit()

    def test_open_constructor_tap_third(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        time.sleep(1)

        mychrome.driver.find_element(By.XPATH, loc.div_third).click()

        time.sleep(1)

        active_tab = mychrome.driver.find_element(By.XPATH, loc.div_current)

        assert active_tab.text == "Начинки"

        mychrome.driver.quit()

    def test_open_constructor_tap_third_then_first(self, existentuser):
        mychrome = MyChrome("https://stellarburgers.nomoreparties.site")
        loc = BurgerLocators()

        time.sleep(1)

        mychrome.driver.find_element(By.XPATH, loc.div_third).click()

        time.sleep(1)

        mychrome.driver.find_element(By.XPATH, loc.div_first).click()

        time.sleep(1)

        active_tab = mychrome.driver.find_element(By.XPATH, loc.div_current)

        assert active_tab.text == "Булки"

        mychrome.driver.quit()
