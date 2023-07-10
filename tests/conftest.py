import random
import pytest
from selenium import webdriver

@pytest.fixture
def new_user():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"qwerty"}
    return user

@pytest.fixture
def invalid_user():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"12345"}
    return user

@pytest.fixture
def existent_user():
    user = {'email':"nataliabruz110606@yandex.ru", 'passw':"qwerty"}
    return user

@pytest.fixture
def my_chrome():
    my_browser = webdriver.Chrome()
    yield my_browser
    my_browser.quit()
