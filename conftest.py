import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, fr, de, es, ru...")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if not language:
        raise pytest.UsageError("--language should be: en, fr, de, es, ru...")

    options = webdriver.ChromeOptions()
    # Убираем сообщения об ошибках при запуске Chrome в Windows 7
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Добавляем язык интерфейса
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
