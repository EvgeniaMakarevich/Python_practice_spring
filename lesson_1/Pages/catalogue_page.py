from lesson_1.Pages.base_page import BasePage
from lesson_1.Locators.catalogue_locators import CatalogueLocators
from selenium.webdriver.common.by import By
from lesson_1.Locators.product_locators import ProductLocators

locators = CatalogueLocators()


class Catalogue(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.item_price = None
        self.item_desc = None
        self.item_name = None

    def add_to_cart_catalogue(self, add_to_cart_locator, cart_button):
        self.visibility_of_element_located(add_to_cart_locator).click()
        self.visibility_of_element_located(cart_button).click()

    def get_item_name_text(self, item_name_locator):
        return self.visibility_of_element_located((By.XPATH, item_name_locator)).text

    def get_item_desc_text(self, item_desc_locator):
        return self.visibility_of_element_located((By.XPATH,item_desc_locator)).text

    def get_item_price_text(self, item_price_locator):
        return self.visibility_of_element_located((By.XPATH, item_price_locator)).text

    def logout(self):
        burger_button = self.clickability_of_element_located(locators.burger_menu)
        burger_button.click()
        logout_button = self.clickability_of_element_located(locators.logout_button)
        logout_button.click()

    def add_to_cart(self, locator):
        self.visibility_of_element_located(locator).click()
        self.visibility_of_element_located(ProductLocators.add_to_cart_button).click()
        self.visibility_of_element_located(locators.cart_button).click()
