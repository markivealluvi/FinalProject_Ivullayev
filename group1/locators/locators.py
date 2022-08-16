from selenium.webdriver.common.by import By


class MainPageLocs:

    rgn_sets_loc = (By.CLASS_NAME, 'fancybox-region')
    crncy_menu_loc = (By.NAME, 'currency_code')
    cntry_menu_loc = (By.NAME, 'country_code')
    save_btn_loc = (By.NAME, 'save')
    crncy_name_loc = (By.CSS_SELECTOR, '[title="US Dollars"]')
    cntry_name_loc = (By.CSS_SELECTOR, '[title="Kazakhstan"]')

    login_input_loc = (By.NAME, 'email')
    login = 'ikram.sharipoff@gmail.com'
    password_input_loc = (By.NAME, 'password')
    password = 'qwerty123'
    login_button_loc = (By.CSS_SELECTOR, '[value="Login"]')

    yellow_duck_loc = (By.CSS_SELECTOR,
                       '[href="http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1"]')


class DuckPageLocs:

    duck_page_title_loc = (By.CSS_SELECTOR, '[style="margin-bottom: 0px;"]')
    add_to_cart_loc = (By.NAME, 'add_cart_product')
    quantity_input_loc = (By.NAME, 'quantity')
    select_size_loc = (By.NAME, 'options[Size]')
    cart_page_loc = (By.XPATH, '//a[@class="content"]')
    duck_quantity = '2'


class CartPageLocs:

    cart_title_loc = (By.XPATH, '//h2[text()="Order Summary"]')
    quantity_loc = (By.CSS_SELECTOR, '[style="text-align: center;"]')
    cost_loc = (By.XPATH, '//td[@class="unit-cost"]')
    total_sum_loc = (By.XPATH, '//td[@class="sum"]')

    first_name_loc = (By.NAME, 'firstname')
    last_name_loc = (By.NAME, 'lastname')
    address1_loc = (By.NAME, 'address1')
    postcode_loc = (By.NAME, 'postcode')
    city_loc = (By.NAME, 'city')
    select_country_loc = (By.XPATH, '//select[@name="country_code"]')
    email_loc = (By.NAME, 'email')
    phone_loc = (By.NAME, 'phone')
    save_changes_button_loc = (By.XPATH, '//td/button[@value="Save Changes"]')

    confirm_button_loc = (By.XPATH, '//button[@name="confirm_order"]')
    order_success_title_loc = (By.CLASS_NAME, 'title')
