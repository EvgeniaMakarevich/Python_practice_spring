from lesson_1.Pages.base_page import BasePage
from lesson_1.Locators.catalogue_locators import CatalogueLocators
from lesson_1.Locators.product_locators import ProductLocators

locators = ProductLocators()


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.item_price = None
        self.item_desc = None
        self.item_name = None

    def add_to_cart_product_page(self):
        self.visibility_of_element_located(locators.add_to_cart_button).click()

        self.item_name = self.visibility_of_element_located(locators.item_name_product_page).text
        self.item_desc = self.visibility_of_element_located(locators.item_desc_product_page).text
        self.item_price = self.visibility_of_element_located(locators.item_price_product_page).text

        self.visibility_of_element_located(CatalogueLocators.cart_button).click()

    def remove_from_cart_product_page(self):
        self.visibility_of_element_located(locators.add_to_cart_button).click()
        self.visibility_of_element_located(locators.remove_button).click()
        self.visibility_of_element_located(CatalogueLocators.cart_button).click()