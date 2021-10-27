from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_products_in_basket(self):
        '''Проверяет, что не появились товары в корзине'''
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Found products in basket"

    def should_be_empty_basket_tag(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TAG), "Not found empty basket tag"
