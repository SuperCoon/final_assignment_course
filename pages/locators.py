from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_LOGIN = (By.ID, 'id_registration-email')
    REG_PASSWORD1 = (By.ID, 'id_registration-password1')
    REG_PASSWORD2 = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')


class ProductPageLocators():
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    NAME_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") 
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1") 
    PRICE_ALERT = (By.CSS_SELECTOR, "div.alertinner > p > strong") 
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color") 
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class BasketPageLocators():
    EMPTHY_MESSAGE = (By.CSS_SELECTOR, "p")
