from selenium.common import NoSuchElementException
from Python_practice_spring.lesson_1.Pages.cart import Cart
from Python_practice_spring.lesson_1.Data.catalogue_data import CatalogueData
from Python_practice_spring.lesson_1.Locators.catalogue_locators import CatalogueLocators
from Python_practice_spring.lesson_1.Locators.cart_locators import CartLocators
from Python_practice_spring.lesson_1.Data.cart_data import CartData
import pytest


class TestCart:
    @pytest.mark.parametrize("add_cart_locator, remove_cart_locator", [
        (CatalogueLocators.add_to_cart_backpack, CartLocators.remove_button_backpack),
        (CatalogueLocators.add_to_cart_bike, CartLocators.remove_button_bike),
        (CatalogueLocators.add_to_cart_jacket, CartLocators.remove_button_jacket),
        (CatalogueLocators.add_to_cart_onesie, CartLocators.remove_button_onesie),
        (CatalogueLocators.add_to_cart_tshirt, CartLocators.remove_button_tshirt),
        (CatalogueLocators.add_to_cart_red_tshirt, CartLocators.remove_button_red_tshirt),
    ])
    def test_remove_from_cart(self, login, add_cart_locator, remove_cart_locator):
        driver = login
        cart = Cart(driver, CartData.cart_page)
        cart.remove_from_cart(add_cart_locator, remove_cart_locator)

        assert driver.find_element(*CartLocators.cont_shopping_button).is_enabled()
        assert driver.find_element(*CartLocators.checkout_button).is_enabled()
        assert driver.current_url == CartData.cart_page

        try:
            driver.find_element(*CartLocators.item_name)
            driver.find_element(*CartLocators.item_desc)
            driver.find_element(*CartLocators.item_name)
            driver.find_element(*CartLocators.item_quantity)
            driver.find_element(*remove_cart_locator)
            assert False
        except NoSuchElementException:
            assert True



    @pytest.mark.parametrize("add_cart_locator, remove_cart_locator", [
        (CatalogueLocators.add_to_cart_backpack, CartLocators.remove_button_backpack),
        (CatalogueLocators.add_to_cart_bike, CartLocators.remove_button_bike),
        (CatalogueLocators.add_to_cart_jacket, CartLocators.remove_button_jacket),
        (CatalogueLocators.add_to_cart_onesie, CartLocators.remove_button_onesie),
        (CatalogueLocators.add_to_cart_tshirt, CartLocators.remove_button_tshirt),
        (CatalogueLocators.add_to_cart_red_tshirt, CartLocators.remove_button_red_tshirt),
    ])
    def test_remove_item_go_catalogue(self, login, add_cart_locator, remove_cart_locator):
        driver = login
        cart = Cart(driver, CartData.cart_page)
        cart.remove_from_cart(add_cart_locator, remove_cart_locator)
        cart.visibility_of_element_located(CartLocators.cont_shopping_button).click()
        try:
            driver.find_element(*CatalogueLocators.cart_badge)
            driver.find_element(*remove_cart_locator)
            assert False
        except NoSuchElementException:
            assert True

        assert driver.find_element(*add_cart_locator).is_enabled()
        assert driver.current_url == CatalogueData.catalogue_page
        assert driver.find_element(*add_cart_locator).text == CatalogueData.add_to_cart_button_text






