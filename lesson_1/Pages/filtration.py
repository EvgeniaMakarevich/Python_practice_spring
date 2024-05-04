from selenium.webdriver.common.by import By

from lesson_1.Locators.catalogue_locators import CatalogueLocators
from lesson_1.Pages.base_page import BasePage
from lesson_1.Locators.filtration_locators import FiltrationLocators
from selenium.webdriver.support.ui import Select


class Filtration(BasePage):

    def get_filtration_dropdown(self):
        self.open()
        dropdown = self.visibility_of_element_located(FiltrationLocators.filtration_dropdown)
        select = Select(dropdown)
        return select

    def filtration_az(self):
        select = self.get_filtration_dropdown()
        select.select_by_index(0)

    def filtration_za(self):
        select = self.get_filtration_dropdown()
        select.select_by_index(1)

    def filtration_low_to_high(self):
        select = self.get_filtration_dropdown()
        select.select_by_index(2)

    def filtration_high_to_low(self):
        select = self.get_filtration_dropdown()
        select.select_by_index(3)

    def filtration_by_index(self, index):
        select = self.get_filtration_dropdown()
        select.select_by_index(index)

    def get_prices_list(self):
        product_prices = self.driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(price.text[1:]) for price in product_prices]
        return product_prices_text

    def get_names_list(self):
        product_names = self.driver.find_elements(By.XPATH, CatalogueLocators.item_name)
        product_names_text = [name.text for name in product_names]
        return product_names_text



