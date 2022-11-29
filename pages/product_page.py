

from .base_page import BasePage
import math
import time


from .locators import ProductPageLocators



class ProductPage(BasePage):

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def find_product(self):
        # add_product = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN)
        return (self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN).text)

    def find_product_price(self):
        add_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return (add_product_price.text)

    def find_product_basket(self):
        return(self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET).text)

    def find_price_basket(self):
        return (self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text)

    def add_to_basket_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)

        alert.accept()

    def comparison_name(self, name1, name2):

        assert name1 + " has been added to your basket." == name2, print("ERROR")
        print("ОК")

    def comparison_price(self, price1, price2):

        assert "Your basket total is now " + price1 == price2, print("ERROR")
        print("ОК")