import time
import pytest
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


links = [
    # Ccылки на товары промо-акции
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # Падающий тест
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    # Ссылки на разные товары
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
]

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    # Запомнить название товара и цену
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    # Нажать кнопку "Добавить в корзину"
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    # Проверить название и цену в сообщениях
    page.check_product_name(product_name)
    page.check_product_price(product_price)


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    # Запомнить название товара и цену
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    # Нажать кнопку "Добавить в корзину"
    page.press_button_add_to_basket()
    # page.solve_quiz_and_get_code()
    # Проверить название и цену в сообщениях
    page.check_product_name(product_name)
    page.check_product_price(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину 
    page.press_button_add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()
    # Тест должен упасть

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину 
    page.press_button_add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_message_disappeared()
    # Тест должен упасть

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.press_view_basket_button()
    # Ожидаем, что в корзине нет товаров
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_products_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_tag()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "AsD$#245^dFx"
        # открыть страницу регистрации
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        # зарегистрировать нового пользователя
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        login_page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара 
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        # Запомнить название товара и цену
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        # Нажать кнопку "Добавить в корзину"
        page.press_button_add_to_basket()
        # Проверить название и цену в сообщениях
        page.check_product_name(product_name)
        page.check_product_price(product_price)
