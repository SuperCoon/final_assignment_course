from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class BasketPage(BasePage): 
   
    def should_be_empthy_basket_message(self):
        empthy_message = self.browser.find_element(*BasketPageLocators.EMPTHY_MESSAGE)
        assert "Your basket is empty" in empthy_message.text, "Empthy message isn't presented, but should be"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ITEMS), \
        "Your basket isn't empthy, but should be"

