from selenium.webdriver.common.by import By


class MainPageLocs:

    rgn_sets_loc = (By.CLASS_NAME, 'fancybox-region')
    crncy_menu_loc = (By.NAME, 'currency_code')
    cntry_menu_loc = (By.NAME, 'country_code')
    save_btn_loc = (By.NAME, 'save')
    crncy_name_loc = (By.CSS_SELECTOR, '[title="US Dollars"]')
    cntry_name_loc = (By.CSS_SELECTOR, '[title="Kazakhstan"]')


class CartPageLocs:

    cart_title_loc = (By.ID, 'cart_title')
