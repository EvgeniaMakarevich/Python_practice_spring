from lesson_1.Pages.login_page import LoginPage
from lesson_1.Data.login_data import Login_page_data
from lesson_1.Locators.login_locators import Sauce_login

data = Login_page_data()
locator = Sauce_login()


class TestLogin:

    def test_login_success(self, driver):
        login_page = LoginPage(driver, data.main_page)
        login_page.login(data.username, data.password)
        assert driver.current_url == data.inventory_page

    def test_login_fail(self, driver):
        login_page = LoginPage(driver, data.main_page)
        login_page.login(data.username_wrong, data.password_wrong)
        wrong_container = login_page.visibility_of_element_located(locator.wrong_container)
        assert driver.current_url == data.main_page
        assert wrong_container.text == data.wrong_container_text
        assert wrong_container.value_of_css_property('background-color') == data.wrong_container_color
