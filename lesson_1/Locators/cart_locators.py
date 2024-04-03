from selenium.webdriver.common.by import By


class CartLocators:
    item_name = (By.XPATH, "//div[@data-test = 'inventory-item-name']")
    item_desc = (By.XPATH, "//div[@data-test = 'inventory-item-desc']")
    item_price = (By.XPATH, "//div[@data-test = 'inventory-item-price']")
    item_quantity = (By.XPATH, "//div[@data-test = 'item-quantity']")
    cont_shopping_button = (By.XPATH, "//button[@data-test = 'continue-shopping']")
    checkout_button = (By.XPATH, "//button[@data-test = 'checkout']")

    remove_button_backpack = (By.XPATH, "//button[@data-test = 'remove-sauce-labs-backpack']")
    remove_button_bike = (By.XPATH, "//button[@data-test = 'remove-sauce-labs-bike-light']")
    remove_button_tshirt = (By.XPATH, "//button[@data-test = 'remove-sauce-labs-bolt-t-shirt']")
    remove_button_jacket = (By.XPATH, "//button[@data-test = 'remove-sauce-labs-fleece-jacket']")
    remove_button_onesie = (By.XPATH, "//button[@data-test = 'remove-sauce-labs-onesie']")
    remove_button_red_tshirt = (By.XPATH, "//button[@data-test = 'remove-test.allthethings()-t-shirt-(red)']")
    remove_button_for_all = (By.XPATH, "//button[@class = 'btn btn_secondary btn_small cart_button']")
