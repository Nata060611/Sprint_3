import random

def generate_new_user():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"qwerty"}
    return user

def generate_invalid_user():
    user = {'name':"Наталья", 'email':"nataliabruz11"+str(random.randint(100,999))+"@yandex.ru", 'passw':"12345"}
    return user

def generate_existent_user():
    user = {'email':"nataliabruz110606@yandex.ru", 'passw':"qwerty"}
    return user