from selenium.webdriver.common.by import By

class ProductLocators:
    add_to_cart_button = (By.XPATH, "//button[@data-test = 'add-to-cart']")
    item_name_product_page = (By.XPATH, "//div[@data-test = 'inventory-item-name']")
    item_desc_product_page = (By.XPATH, "//div[@data-test = 'inventory-item-desc']")
    item_price_product_page = (By.XPATH, "//div[@data-test = 'inventory-item-price']")

    remove_button = (By.XPATH, "//button[@data-test = 'remove']")