from pages.base_page import BasePage
from pages.locators import ProductPageLocators

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


