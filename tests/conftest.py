import pytest
from selenium import webdriver

@pytest.fixture
def my_chrome():
    my_browser = webdriver.Chrome()
    yield my_browser
    my_browser.quit()
