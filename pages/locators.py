from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REP_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main:nth-child(2) > h1:nth-child(1)")
    ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alertinner :nth-child(1)")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info >.alertinner :nth-child(1) :nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main >.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini :nth-child(2) >a")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner >p")
    FULL_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    