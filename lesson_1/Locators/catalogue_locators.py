from selenium.webdriver.common.by import By


class CatalogueLocators:
    add_to_cart_backpack = (By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-backpack']")
    add_to_cart_bike = (By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-bike-light']")
    add_to_cart_tshirt = (By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-bolt-t-shirt']")
    add_to_cart_jacket = (By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-fleece-jacket']")
    add_to_cart_onesie = (By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-onesie']")
    add_to_cart_red_tshirt = (By.XPATH, "//button[@data-test = 'add-to-cart-test.allthethings()-t-shirt-(red)']")
    item_name = "//div[@data-test = 'inventory-item-name']"
    item_desc = "//div[@data-test = 'inventory-item-desc']"
    item_price = "//div[@data-test = 'inventory-item-price']"
    item_image = "//div[@class = 'inventory_item_img']"


    cart_button = (By.XPATH, "//a[@data-test = 'shopping-cart-link']")
    cart_badge = (By.XPATH, "//span[@data-test = 'shopping-cart-badge']")

    burger_menu = (By.XPATH, "//button[@id ='react-burger-menu-btn']")
    logout_button = (By.XPATH, "//a[@id ='logout_sidebar_link']")

    items_list_names = [(By.XPATH, '//a[@data-test="item-4-title-link"]'),
    (By.XPATH, '//a[@data-test="item-0-title-link"]'),
    (By.XPATH, '//a[@data-test="item-1-title-link"]'),
    (By.XPATH,'//a[@data-test="item-5-title-link"]'),
    (By.XPATH, '//a[@data-test="item-2-title-link"]'),
    (By.XPATH, '//a[@data-test="item-3-title-link"]')]
