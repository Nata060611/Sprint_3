import random
import pytest

@pytest.fixture # фикстура, которая создаёт НОВОГО пользователя
def newuser():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"qwerty"}
    return user

@pytest.fixture # фикстура, которая создаёт пользователя С НЕВЕРНЫМ ПАРОЛЕМ
def invaliduser():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"12345"}
    return user

@pytest.fixture # фикстура, которая создаёт СУЩЕСТВУЮЩЕГО пользователя
def existentuser():
    user = {'email':"nataliabruz110606@yandex.ru", 'passw':"qwerty"}
    return user

