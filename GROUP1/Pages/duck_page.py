from GROUP1.Pages.base_page import BasePage
from GROUP1.Locators.locators import DuckPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class DuckPage(BasePage):

    def verify_it_is_duck_page(self):
        assert self.is_element_present(DuckPageLocs.duck_page_title_loc), 'It is not the duck page'

    def choose_quantity(self):
        quantity_input = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located
                                                             (DuckPageLocs.quantity_input_loc))
        quantity_input.clear()
        quantity_input.send_keys(DuckPageLocs.duck_quantity)

    def select_size(self):
        select_size = Select(WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                                  (DuckPageLocs.select_size_loc)))
        select_size.select_by_value('Small')

    def add_duck_to_cart(self):
        add_button = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable
                                                         (DuckPageLocs.add_to_cart_loc))
        add_button.click()

    def open_cart_page(self):
        cart_link = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(DuckPageLocs.cart_page_loc))
        time.sleep(1)
        cart_link.click()

