from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class ProductPage(BasePage): 
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
        button.click()

    def product_added(self):
        name_alert = self.browser.find_element(*ProductPageLocators.NAME_ALERT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == name_alert.text, "The name alert doesn't match the product name"

        price_alert = self.browser.find_element(*ProductPageLocators.PRICE_ALERT)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == price_alert.text, "The price alert doesn't match the product price"

        print("The product successfully added")

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.SUBMIT_BUTTON), "Add to basket button is not presented"
