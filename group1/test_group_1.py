import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from pages.duck_page import DuckPage
from pages.cart_page import CartPage
from pages.edit_page import EditPage
from api_petstore import PetStoreApi


@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


def test_changing_currency_and_region_and_verifying_changes(open_browser):

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


def test_adding_to_cart_and_verifying_order_is_made_in_db(open_browser):
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
        duck_page.choose_quantity(2)
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
        cart_page.verify_cost_and_quantity('2')
    with allure.step('Confirm order'):
        cart_page.confirm_order()
        cart_page.order_success()
    with allure.step('Verify the order is made in database'):
        cart_page.verify_db_order()


def test_api_adding_to_and_removing_from_store_of_pet():
    with allure.step('Add new pet to store'):
        PetStoreApi.add_new_pet()
    with allure.step('Verify the pet is added'):
        PetStoreApi.verify_new_pet()
    with allure.step('Delete created pet'):
        PetStoreApi.delete_pet()
    with allure.step('Verify the pet is deleted'):
        PetStoreApi.verify_pet_deleted()


def test_editing_account_and_verifying_the_db_changes(open_browser):

    url = 'http://localhost/litecart/'
    with allure.step('Open application'):
        main_page = MainPage(open_browser, url)
        main_page.open()
    with allure.step('Log in'):
        main_page.login_to_site()
    with allure.step('Open account edit page'):
        main_page.open_edit_page()
    with allure.step('Verify it is edit page'):
        edit_page = EditPage(open_browser, open_browser.current_url)
        edit_page.verify_it_is_edit_page()
    with allure.step('Edit first name of account'):
        edit_page.edit_first_name()
    with allure.step('Click save button'):
        edit_page.save_all()
    with allure.step('Verify name has changed in database'):
        edit_page.verify_db_name_change()


def test_verifying_adding_and_removing_ducks_to_cart(open_browser):
    url = 'http://localhost/litecart/'
    main_page = MainPage(open_browser, url)
    main_page.open()
    with allure.step('Choose yellow duck'):
        main_page.open_duck_page()
    with allure.step('Verify it is the yellow duck page'):
        duck_page = DuckPage(open_browser, open_browser.current_url)
        duck_page.verify_it_is_duck_page()
    with allure.step('Select size of duck'):
        duck_page.select_size()
    with allure.step('Add the product to cart'):
        duck_page.add_duck_to_cart()
    with allure.step('Open the cart page'):
        duck_page.open_cart_page()
    with allure.step('Change ducks quantity'):
        cart_page = CartPage(open_browser, open_browser.current_url)
        cart_page.change_duck_quantity('3')
    with allure.step('Verify the quantity and total sum of cart'):
        cart_page.verify_cost_and_quantity('3')
    with allure.step('Remove ducks from cart'):
        cart_page.remove_ducks()
    with allure.step('Verify the cart is empty'):
        cart_page.verify_ducks_were_removed()


def test_api_changing_username():
    with allure.step('Add new user'):
        PetStoreApi.create_user()
    with allure.step('Get new users data'):
        PetStoreApi.get_user_data()
    with allure.step('Update username'):
        PetStoreApi.update_username()
    with allure.step('Verify username has changed'):
        PetStoreApi.verify_username_changed()
