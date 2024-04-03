from Python_practice_spring.lesson_1.Pages.catalogue_page import Catalogue
from Python_practice_spring.lesson_1.Locators.catalogue_locators import CatalogueLocators
from Python_practice_spring.lesson_1.Locators.cart_locators import CartLocators
from Python_practice_spring.lesson_1.Data.catalogue_data import CatalogueData
from Python_practice_spring.lesson_1.Data.cart_data import CartData
from Python_practice_spring.lesson_1.Data.login_data import Login_page_data
import pytest

locators = CatalogueLocators()
data = CatalogueData


class TestAddToCart:
    @pytest.mark.parametrize("add_to_cart_locator, item_index", [
        (CatalogueLocators.add_to_cart_backpack, 1),
        (CatalogueLocators.add_to_cart_bike, 2),
        (CatalogueLocators.add_to_cart_tshirt, 3),
        (CatalogueLocators.add_to_cart_jacket, 4),
        (CatalogueLocators.add_to_cart_onesie, 5),
        (CatalogueLocators.add_to_cart_red_tshirt, 6)
    ])
    def test_add_to_cart_and_verify_product(self, login, add_to_cart_locator, item_index):
        driver = login
        catalogue = Catalogue(driver, data.catalogue_page)

        # Получаем информацию о товаре перед добавлением в корзину
        item_name = catalogue.get_item_name_text(f'({CatalogueLocators.item_name})[{item_index}]')
        item_desc = catalogue.get_item_desc_text(f'({CatalogueLocators.item_desc})[{item_index}]')
        item_price = catalogue.get_item_price_text(f'({CatalogueLocators.item_price})[{item_index}]')


        # Добавление товара в корзину
        catalogue.add_to_cart_catalogue(add_to_cart_locator, CatalogueLocators.cart_button)

        # Проверка перехода на страницу корзины
        assert driver.current_url == CartData.cart_page, "Not redirected to cart page after adding item"

        # Проверка отображения добавленного товара в корзине
        assert driver.find_element(*CartLocators.item_name).text == item_name, "Item name not found in cart or item details mismatch"
        assert driver.find_element(*CartLocators.item_desc).text == item_desc, "Item desc not found in cart or item details mismatch"
        assert driver.find_element(*CartLocators.item_price).text == item_price, "Item price not found in cart or item details mismatch"
        assert driver.find_element(*CartLocators.item_quantity).text == '1'


    def test_add_to_cart_and_go_to_catalogue(self, login):
        driver = login
        catalogue = Catalogue(driver, data.catalogue_page)
        catalogue.add_to_cart_catalogue(CatalogueLocators.add_to_cart_tshirt, CatalogueLocators.cart_button)
        catalogue.visibility_of_element_located(CartLocators.cont_shopping_button).click()

        assert driver.current_url == CatalogueData.catalogue_page
        assert catalogue.visibility_of_element_located(CartLocators.remove_button_tshirt).is_displayed() == True
        assert catalogue.visibility_of_element_located(CatalogueLocators.cart_badge).text == '1'
        assert catalogue.visibility_of_element_located(CartLocators.remove_button_tshirt).value_of_css_property('color') == Login_page_data.wrong_container_color
