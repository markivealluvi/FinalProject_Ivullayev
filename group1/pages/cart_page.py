import time
from group1.pages.base_page import BasePage
from group1.locators.locators import CartPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from group1.sql_helper import MySQL


class CartPage(BasePage):

    def verify_it_is_cart_page(self):
        WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                             (CartPageLocs.cart_title_loc))
        assert self.is_element_present(CartPageLocs.cart_title_loc), 'It is not the cart page'

    def verify_cost_and_quantity(self, quantity):
        total_quantity = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                              (CartPageLocs.cart_quantity_loc)).text
        total_sum = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                         (CartPageLocs.total_sum_loc)).text
        cost = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                    (CartPageLocs.cost_loc)).text
        total_sum = total_sum[1:3]
        cost = cost[1:3]
        result = float(cost) * int(total_quantity)
        result = str(result)[:2]
        print(total_quantity, total_sum, cost, result, quantity)
        assert total_quantity == quantity
        assert total_sum == result

    def confirm_order(self):
        confirm_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable
                                                              (CartPageLocs.confirm_button_loc))
        confirm_button.click()

    def order_success(self):
        assert WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                    (CartPageLocs.order_success_title_loc))

    @staticmethod
    def verify_db_order():
        db = MySQL.create_connection()
        query = MySQL.query_orders
        result = MySQL.execute_read_query(db, query)
        assert 'Marco', 'Reus' in result
        MySQL.close_db(db)


    # @staticmethod
    # def verify_db_order():
    #     db = mysql.connect(host="127.0.0.1",
    #                        user="root",
    #                        passwd="",
    #                        database="litecart")
    #     cursor = db.cursor()
    #     query = 'SELECT * FROM `lc_orders`'
    #     cursor.execute(query)
    #     assert 'Marco', 'Reus' in query

    def change_duck_quantity(self, quantity):
        duck_quantity = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                             (CartPageLocs.quantity_of_ducks_loc))
        duck_quantity.clear()
        duck_quantity.send_keys(quantity)
        update_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(CartPageLocs.update_button_loc))
        update_button.click()
        time.sleep(3)

    def remove_ducks(self):
        remove_button = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(CartPageLocs.remove_button_loc))
        remove_button.click()

    def verify_ducks_were_removed(self):
        title = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located
                                                     (CartPageLocs.removed_title_loc)).text
        assert title == 'There are no items in your cart.'
