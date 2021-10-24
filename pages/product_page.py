from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text
        product_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text
        
        self.find_element(ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.check_messages(product_name, product_price)

    def check_messages(self, product_name, product_price):
        lst = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert len(lst) == 3, "Success message not found"

        assert product_name == lst[0].text, "Wrong name product added to basket"
        assert product_price == lst[2].text, "Wrong price product added to basket"
