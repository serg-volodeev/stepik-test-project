from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.product_name = self.element_text(ProductPageLocators.PRODUCT_NAME)
        self.product_price = self.element_text(ProductPageLocators.PRODUCT_PRICE)
        self.click_element(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def element_text(self, locator):
        return self.find_element(locator).text

    def click_element(self, locator):
        self.find_element(locator).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
