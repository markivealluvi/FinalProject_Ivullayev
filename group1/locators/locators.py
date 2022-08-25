from selenium.webdriver.common.by import By


class MainPageLocs:

    rgn_sets_loc = (By.CLASS_NAME, 'fancybox-region')
    crncy_menu_loc = (By.NAME, 'currency_code')
    cntry_menu_loc = (By.NAME, 'country_code')
    save_btn_loc = (By.NAME, 'save')
    crncy_name_loc = (By.CSS_SELECTOR, '[title="US Dollars"]')
    cntry_name_loc = (By.CSS_SELECTOR, '[title="Kazakhstan"]')

    login_input_loc = (By.NAME, 'email')
    login = 'strange@gmail.com'
    password_input_loc = (By.NAME, 'password')
    password = 'qwerty123'
    login_button_loc = (By.CSS_SELECTOR, '[value="Login"]')

    cart_page_loc = (By.XPATH, '//a[@class="content"]')
    cart_quantity_loc = (By.CLASS_NAME, 'quantity')

    yellow_duck_loc = (By.CSS_SELECTOR,
                       '[href="http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1"]')

    edit_acc_loc = (By.XPATH, '//div/ul/li/a[@href="http://localhost/litecart/en/edit_account"]')


class DuckPageLocs:

    duck_page_title_loc = (By.CSS_SELECTOR, '[style="margin-bottom: 0px;"]')
    add_to_cart_loc = (By.NAME, 'add_cart_product')
    quantity_input_loc = (By.NAME, 'quantity')
    select_size_loc = (By.NAME, 'options[Size]')
    cart_page_loc = (By.XPATH, '//a[@class="content"]')
    duck_quantity = '2'


class CartPageLocs:

    cart_title_loc = (By.XPATH, '//h2[text()="Order Summary"]')
    cart_quantity_loc = (By.XPATH, '//td[@style="text-align: center;"]')
    remove_button_loc = (By.NAME, 'remove_cart_item')
    removed_title_loc = (By.XPATH, '//em')
    main_page_loc = (By.XPATH, '//p/a[@href="http://localhost/litecart/en/"]')
    quantity_loc = (By.CSS_SELECTOR, '[style="text-align: center;"]')
    cost_loc = (By.XPATH, '//td[@class="unit-cost"]')
    total_sum_loc = (By.XPATH, '//td[@class="sum"]')

    first_name_loc = (By.XPATH, '//input[@name="firstname"]')
    firstname = 'Marco'
    last_name_loc = (By.XPATH, '//input[@name="lastname"]')
    lastname = 'Reus'
    address1_loc = (By.XPATH, '//input[@name="address1"]')
    address = 'District 10'
    city_loc = (By.XPATH, '//input[@name="city"]')
    city = 'Almaty'
    select_country_loc = (By.XPATH, '//select[@name="country_code"]')
    phone_loc = (By.XPATH, '//input[@name="phone"]')
    phone = '87759827882'
    save_changes_button_loc = (By.XPATH, '//td/button[@value="Save Changes"]')

    confirm_button_loc = (By.XPATH, '//button[@name="confirm_order"]')
    order_success_title_loc = (By.CLASS_NAME, 'title')
    quantity_of_ducks_loc = (By.NAME, 'quantity')
    update_button_loc = (By.NAME, 'update_cart_item')


class EditPageLocs:

    edit_title = (By.CLASS_NAME, 'title')
    first_name_loc = (By.NAME, 'firstname')
    save_button_loc = (By.CSS_SELECTOR, '[type="submit"]')
