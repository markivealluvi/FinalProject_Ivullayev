from group1.pages.base_page import BasePage
from group1.locators.locators import CartPageLocs
from group1.locators.locators import DuckPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import mysql.connector as mysql


class CartPage(BasePage):

    def verify_it_is_cart_page(self):
        WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                             (CartPageLocs.cart_title_loc))
        assert self.is_element_present(CartPageLocs.cart_title_loc), 'It is not the cart page'

    def verify_quantity_of_ducks(self):
        assert WebDriverWait(self.chrome, 20).until(EC.text_to_be_present_in_element(CartPageLocs.quantity_loc,
                                                                                     DuckPageLocs.duck_quantity))

    @staticmethod
    def verify_cost_of_ducks():
        tuple_cost = CartPageLocs.cost_loc
        cost = [x[0] for x in tuple_cost]
        tuple_sum = CartPageLocs.total_sum_loc
        total_sum = [x[0] for x in tuple_sum]
        assert cost[0] == total_sum[0]

    def credentials_input(self):
        first_name = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                          (CartPageLocs.first_name_loc))
        first_name.send_keys('Marco')

        last_name = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                         (CartPageLocs.last_name_loc))
        last_name.send_keys('Reus')

        address1 = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                        (CartPageLocs.address1_loc))
        address1.send_keys('micro-district 10')

        postcode = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                        (CartPageLocs.postcode_loc))
        postcode.send_keys('050036')

        city = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                    (CartPageLocs.city_loc))
        city.send_keys('Almaty')

        country = Select(WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                              (CartPageLocs.select_country_loc)))
        country.select_by_value('KZ')

        email_input = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                           (CartPageLocs.email_loc))
        email_input.send_keys('marco@gmail.com')

        phone = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                     (CartPageLocs.phone_loc))
        phone.send_keys('+375259157313')
        save_changes_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                                   (CartPageLocs.save_changes_button_loc))
        save_changes_button.click()

    def confirm_order(self):
        confirm_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                              (CartPageLocs.confirm_button_loc))
        confirm_button.click()

    def order_success(self):
        assert WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located
                                                    (CartPageLocs.order_success_title_loc))

    @staticmethod
    def verify_db_order():

        db = mysql.connect(host="127.0.0.1",
                           user="root",
                           passwd="",
                           database="litecart")
        cursor = db.cursor()
        query = 'SELECT * FROM `lc_orders`'
        cursor.execute(query)
        assert 'Marco', 'Reus' in query
