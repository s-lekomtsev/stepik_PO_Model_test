from .base_page import BasePage
from .product_page import ProductPage
from .locators import BasketPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            "Basket is not empty"

    def find_basket_is_empty_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        return (empty_basket_text.text)

    # для тестирования
    def add_to_basket_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()

