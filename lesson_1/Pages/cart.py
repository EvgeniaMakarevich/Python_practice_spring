from lesson_1.Pages.base_page import BasePage
from lesson_1.Locators.catalogue_locators import CatalogueLocators


class Cart(BasePage):
    def remove_from_cart(self, add_to_cart_item_button, remove_button):
        self.visibility_of_element_located(add_to_cart_item_button).click()
        self.visibility_of_element_located(CatalogueLocators.cart_button).click()
        self.visibility_of_element_located(remove_button).click()