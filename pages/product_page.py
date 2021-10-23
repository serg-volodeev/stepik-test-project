from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.product_name = self.text(ProductPageLocators.PRODUCT_NAME)
        self.product_price = self.text(ProductPageLocators.PRODUCT_PRICE)
        self.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        self.should_be(ProductPageLocators.ADD_TO_BASKET_BUTTON)
