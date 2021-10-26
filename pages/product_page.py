from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        
        product_name_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG).text
        product_price_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MSG).text
        
        assert product_name == product_name_msg, "Wrong name product added to basket"
        assert product_price == product_price_msg, "Wrong price product added to basket"

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def press_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_product_name(self, product_name):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_MSG), "Product name is not presented in message"
        product_name_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG).text
        assert product_name == product_name_msg, "Wrong name product added to basket"

    def check_product_price(self, product_price):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_MSG), "Product price is not presented in message"
        product_price_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MSG).text
        assert product_price == product_price_msg, "Wrong price product added to basket"

    def should_not_be_success_message(self):
        '''Сообщение не должно появиться'''
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_message_disappeared(self):
        '''Сообщение должно исчезнуть'''
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        