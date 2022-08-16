import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from GROUP1.Pages.main_page import MainPage
from GROUP1.Pages.duck_page import DuckPage
from GROUP1.Pages.cart_page import CartPage
from GROUP1.api_petstore import PetStoreApi


@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


def test_tc_1(open_browser):

    url = 'http://localhost/litecart/'
    with allure.step('Open application'):
        main_page = MainPage(open_browser, url)
        main_page.open()
    with allure.step('Open regional settings'):
        main_page.open_region_settings()
    with allure.step('Change currency and region'):
        main_page.change_currency()
        main_page.change_region()
        main_page.save_all()
    with allure.step('Verify currency and region have been changed'):
        main_page.verify_currency_is_changed()
        main_page.verify_region_is_changed()


def test_tc_2(open_browser):
    url = 'http://localhost/litecart/'
    with allure.step('Open application'):
        main_page = MainPage(open_browser, url)
        main_page.open()
    with allure.step('Log in'):
        main_page.login_to_site()
    with allure.step('Choose yellow duck'):
        main_page.open_duck_page()
    with allure.step('Verify it is the yellow duck page'):
        duck_page = DuckPage(open_browser, open_browser.current_url)
        duck_page.verify_it_is_duck_page()
    with allure.step('Choose quantity of duck'):
        duck_page.choose_quantity()
    with allure.step('Select size of duck'):
        duck_page.select_size()
    with allure.step('Add the product to cart'):
        duck_page.add_duck_to_cart()
    with allure.step('Open the cart page'):
        duck_page.open_cart_page()
    with allure.step('Verify it is the cart page'):
        cart_page = CartPage(open_browser, open_browser.current_url)
        cart_page.verify_it_is_cart_page()
    with allure.step('Verify the quantity and cost of product'):
        cart_page.verify_quantity_of_ducks()
        cart_page.verify_cost_of_ducks()
    with allure.step('Input credentials'):
        cart_page.credentials_input()
        cart_page.confirm_order()
        cart_page.order_success()
    with allure.step('Verify the order is made'):
        cart_page.verify_db_order()


def test_api():
    with allure.step('Add new pet to store'):
        PetStoreApi.add_new_pet()
    with allure.step('Verify the pet is added'):
        PetStoreApi.verify_new_pet()
    with allure.step('Delete created pet'):
        PetStoreApi.delete_pet()
    with allure.step('Verify the pet is deleted'):
        PetStoreApi.verify_pet_deleted()
