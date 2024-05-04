import time

import pytest
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
        price_list = filtration.get_prices_list()
        assert price_list == sorted(price_list)

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
        price_list = filtration.get_prices_list()
        assert price_list == sorted(price_list, reverse=True)

    def test_filtration_high_to_low_v2(self, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_high_to_low()
        product_prices = driver.find_elements(By.XPATH, CatalogueLocators.item_price)
        product_prices_text = [float(''.join(re.findall(r'[\d,.]+', price.text))) for price in product_prices]
        assert product_prices_text == sorted(product_prices_text, reverse=True)

    @pytest.mark.parametrize('value', ([2, False], [3, True]))
    def test_filtration_by_price(self, value, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_by_index(value[0])
        price_list = filtration.get_prices_list()
        assert price_list == sorted(price_list, reverse=value[1])

    @pytest.mark.parametrize('value', ([0, False], [1, True]))
    def test_filtration_by_name(self, value, login):
        driver = login
        filtration = Filtration(driver, CatalogueData.catalogue_page)
        filtration.filtration_by_index(value[0])
        name_list = filtration.get_names_list()
        assert name_list == sorted(name_list, reverse=value[1])
