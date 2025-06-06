from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.get('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REG_LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

   
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"