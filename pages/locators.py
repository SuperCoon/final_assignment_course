from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    NAME_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") 
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1") 
    PRICE_ALERT = (By.CSS_SELECTOR, "div.alertinner > p > strong") 
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color") 
