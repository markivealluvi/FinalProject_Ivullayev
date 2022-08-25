from group1.pages.base_page import BasePage
from group1.locators.locators import EditPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector as mysql


class EditPage(BasePage):

    def verify_it_is_edit_page(self):
        edit_page_title = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(EditPageLocs.edit_title))
        assert edit_page_title.text == 'Edit Account'

    def edit_first_name(self):
        first_name_input = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located
                                                               (EditPageLocs.first_name_loc))
        first_name_input.clear()
        first_name_input.send_keys('Erling')

    def save_all(self):
        save_button = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable(EditPageLocs.save_button_loc))
        save_button.click()

    @staticmethod
    def verify_db_name_change():

        db = mysql.connect(host="127.0.0.1",
                           user="root",
                           passwd="",
                           database="litecart")
        cursor = db.cursor()
        query = "SELECT firstname FROM `lc_customers`"
        cursor.execute(query)
        firstname = cursor.fetchall()
        firstnames = []
        for element in firstname:
            firstnames.append(element[0])
        assert 'Erling' in firstnames
