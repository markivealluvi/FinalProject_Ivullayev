import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from GROUP1_TC_1.Pages.main_page import MainPage


@pytest.fixture(scope='module')
def open_browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


def test_open_shop(open_browser):

    url = 'http://localhost/litecart/'
    global main_page
    main_page = MainPage(open_browser, url)
    main_page.open()


def test_change_settings():

    main_page.open_region_settings()
    main_page.change_currency()
    main_page.change_region()
    main_page.save_all()


def test_verify_changes():

    main_page.verify_currency_is_changed()
    main_page.verify_region_is_changed()
