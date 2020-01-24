from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_button.click()

    def check_product_name_in_cart(self):
        name1 = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        name2 = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT).text
        assert name1 == name2, "Product title and product title in cart do not match."
    
    def check_product_price_in_cart(self):
        price1 = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        price2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price1 == price2, "Product price and price in cart do not match."

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    

