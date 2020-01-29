from pages.locators import BasketPageLocators
from pages.base_page import BasePage

class BasketPage(BasePage):
    def should_not_see_products_basket(self):
        assert not self.is_element_present(*BasketPageLocators.FULL_BASKET), "The basket is not empty"

    def should_see_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No text for empty basket"
        #content_inner >p
        #basket_formset