from GROUP1_TC_1.Pages.base_page import BasePage
from GROUP1_TC_1.Locators.locators import MainPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def open_region_settings(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.rgn_sets_loc))
        region_settings = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLocs.rgn_sets_loc))
        region_settings.click()

    def change_currency(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.crncy_menu_loc))
        currency_menu = Select(WebDriverWait(self.chrome, 20).until
                               (EC.element_to_be_clickable(MainPageLocs.crncy_menu_loc)))
        currency_menu.select_by_value('USD')

    def change_region(self):
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.cntry_menu_loc))
        region_menu = Select(WebDriverWait(self.chrome, 20).until
                             (EC.element_to_be_clickable(MainPageLocs.cntry_menu_loc)))
        region_menu.select_by_value('KZ')

    def save_all(self):
        save_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLocs.save_btn_loc))
        save_button.click()

    def verify_currency_is_changed(self):
        assert self.is_element_present(MainPageLocs.crncy_name_loc), 'The currency has changed successfully!'

    def verify_region_is_changed(self):
        assert self.is_element_present(MainPageLocs.cntry_name_loc), 'The region has changed successfully!'
