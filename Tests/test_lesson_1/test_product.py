from selenium.webdriver.common.by import By
from lesson_1.Pages.product_page import ProductPage
from lesson_1.Locators.catalogue_locators import CatalogueLocators
from lesson_1.Locators.cart_locators import CartLocators
from lesson_1.Data.catalogue_data import CatalogueData
from lesson_1.Data.cart_data import CartData
from lesson_1.Locators.product_locators import ProductLocators


class TestProduct:
    def test_add_to_cart_product_page(self, login):
        driver = login
        products = ProductPage(driver, CatalogueData.catalogue_page)

        x = 1
        for item in range(6):
            item_name = driver.find_element(By.XPATH, f"({CatalogueLocators.item_name})[{x}]")
            x += 1
            item_name.click()
            products.add_to_cart_product_page()
            assert driver.current_url == CartData.cart_page
            assert driver.find_element(
                *CartLocators.item_name).text == products.item_name, "Item name not found in cart or item details mismatch"
            assert driver.find_element(
                *CartLocators.item_desc).text == products.item_desc, "Item desc not found in cart or item details mismatch"
            assert driver.find_element(
                *CartLocators.item_price).text == products.item_price, "Item price not found in cart or item details mismatch"
            assert driver.find_element(*CartLocators.item_quantity).text == '1'

            driver.find_element(*CartLocators.remove_button_for_all).click()
            products.open()

    def test_remove_from_cart_product_page(self, login):
        driver = login
        products = ProductPage(driver, CatalogueData.catalogue_page)
        x = 1
        for item in range(6):
            item_name = driver.find_element(By.XPATH, f"({CatalogueLocators.item_name})[{x}]")
            x += 1
            item_name.click()
            products.remove_from_cart_product_page()

            assert driver.current_url == CartData.cart_page
            assert products.visibility_of_element_not_located(CartLocators.item_name), "Item name remains in the cart"
            assert products.visibility_of_element_not_located(CartLocators.item_desc), "Item desc remains in the cart"
            assert products.visibility_of_element_not_located(CartLocators.item_price), "Item price remains in the cart"

            driver.back()

            assert products.visibility_of_element_not_located(ProductLocators.remove_button), "Remove button remains on the product page"
            assert products.visibility_of_element_located(ProductLocators.add_to_cart_button), "Add_to_cart button is absent on the product page"
            assert products.visibility_of_element_not_located(CatalogueLocators.cart_badge), "Cart badge shows the number of items in the cart"
            products.open()


    def test_open_product_image_click(self, login):
        driver = login
        products = ProductPage(driver, CatalogueData.catalogue_page)
        x = 1
        for item in range(6):
            item_image = driver.find_element(By.XPATH, f"({CatalogueLocators.item_image})[{x}]")
            item_name_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_name})[{x}]").text
            item_desc_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_desc})[{x}]").text
            item_price_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_price})[{x}]").text
            x += 1
            item_image.click()
            assert driver.current_url.startswith('https://www.saucedemo.com/inventory-item.')
            assert item_name_text == products.visibility_of_element_located(ProductLocators.item_name_product_page).text
            assert item_desc_text == products.visibility_of_element_located(ProductLocators.item_desc_product_page).text
            assert item_price_text == products.visibility_of_element_located(ProductLocators.item_price_product_page).text

            products.open()


    def test_open_product_title_click(self, login):
        driver = login
        products = ProductPage(driver, CatalogueData.catalogue_page)
        x = 1
        for item in range(6):
            item_name = driver.find_element(By.XPATH, f"({CatalogueLocators.item_name})[{x}]")
            item_name_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_name})[{x}]").text
            item_desc_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_desc})[{x}]").text
            item_price_text = driver.find_element(By.XPATH, f"({CatalogueLocators.item_price})[{x}]").text
            x += 1
            item_name.click()
            assert driver.current_url.startswith('https://www.saucedemo.com/inventory-item.')
            assert item_name_text == products.visibility_of_element_located(ProductLocators.item_name_product_page).text
            assert item_desc_text == products.visibility_of_element_located(ProductLocators.item_desc_product_page).text
            assert item_price_text == products.visibility_of_element_located(ProductLocators.item_price_product_page).text

            products.open()



