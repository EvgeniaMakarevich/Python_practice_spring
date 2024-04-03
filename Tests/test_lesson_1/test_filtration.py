from selenium.webdriver.common.by import By
from lesson_1.Locators.catalogue_locators import CatalogueLocators
from lesson_1.Pages.filtration import Filtration
from lesson_1.Data.catalogue_data import CatalogueData
import re
# from conftest import login, driver, options


class TestFiltration:

    def test_filtration_az(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_az()
        product_names = driver.find_elements(By.XPATH, CatalogueLocators.item_name)
        product_names_text = [name.text for name in product_names]
        assert product_names_text == sorted(product_names_text)

    def test_filtration_za(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_za()
        product_names = driver.find_elements(By.XPATH, CatalogueLocators.item_name)
        product_names_text = [name.text for name in product_names]
        assert product_names_text == sorted(product_names_text, reverse=True)

    def test_filtration_low_to_high_v1(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_low_to_high()
        product_prices = driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(price.text[1:]) for price in product_prices]
        assert product_prices_text == sorted(product_prices_text)

    def test_filtration_low_to_high_v2(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_low_to_high()
        product_prices = driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(''.join(re.findall(r'[\d,.]+', price.text))) for price in product_prices]
        assert product_prices_text == sorted(product_prices_text)

    def test_filtration_high_to_low_v1(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_high_to_low()
        product_prices = driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(price.text[1:]) for price in product_prices]
        assert product_prices_text == sorted(product_prices_text, reverse=True)

    def test_filtration_high_to_low_v2(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_high_to_low()
        product_prices = driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(''.join(re.findall(r'[\d,.]+', price.text))) for price in product_prices]
        assert product_prices_text == sorted(product_prices_text, reverse=True)