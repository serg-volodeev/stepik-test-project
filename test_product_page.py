import pytest
from pages.product_page import ProductPage


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
def test_guest_can_add_product_to_basket(browser, link):
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

@pytest.mark.skip
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

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину 
    page.press_button_add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_message_disappeared()
    # Тест должен упасть
