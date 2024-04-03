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