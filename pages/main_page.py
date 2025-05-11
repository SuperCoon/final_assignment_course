from .base_page import BasePage
from .locators import BasePageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

#В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)