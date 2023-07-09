from selenium import webdriver

# класс для работы с браузером
class MyChrome:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
