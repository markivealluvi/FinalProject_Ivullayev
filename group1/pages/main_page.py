from group1.pages.base_page import BasePage
from group1.locators.locators import MainPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def open_region_settings(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.rgn_sets_loc))
        region_settings = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                               (MainPageLocs.rgn_sets_loc))
        region_settings.click()

    def change_currency(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.crncy_menu_loc))
        currency_menu = Select(WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                                    (MainPageLocs.crncy_menu_loc)))
        currency_menu.select_by_value('USD')

    def change_region(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.cntry_menu_loc))
        region_menu = Select(WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                                  (MainPageLocs.cntry_menu_loc)))
        region_menu.select_by_value('KZ')

    def save_all(self):
        save_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLocs.save_btn_loc))
        save_button.click()

    def verify_currency_is_changed(self):
        assert self.is_element_present(MainPageLocs.crncy_name_loc), 'The currency hasn\'t been changed!'

    def verify_region_is_changed(self):
        assert self.is_element_present(MainPageLocs.cntry_name_loc), 'The region hasn\'t been changed!'

    def login_to_site(self):
        login_input = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located
                                                          (MainPageLocs.login_input_loc))
        login_input.send_keys(MainPageLocs.login)
        password_input = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located
                                                             (MainPageLocs.password_input_loc))
        password_input.send_keys(MainPageLocs.password)
        login_button = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable
                                                           (MainPageLocs.login_button_loc))
        login_button.click()

    def open_cart_page(self):
        cart_link = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(MainPageLocs.cart_page_loc))
        cart_link.click()

    def open_duck_page(self):
        yellow_duck = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located
                                                          (MainPageLocs.yellow_duck_loc))
        yellow_duck.click()

    def open_edit_page(self):
        edit_acc = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLocs.edit_acc_loc))
        edit_acc.click()
