from Python_practice_spring.lesson_1.Pages.base_page import BasePage
from Python_practice_spring.lesson_1.Locators.catalogue_locators import CatalogueLocators
from selenium.webdriver.common.by import By

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