from selenium.webdriver.common.by import By

from lesson_1.Pages.base_page import BasePage
from lesson_1.Data.login_data import Login_page_data
from lesson_1.Locators.login_locators import Sauce_login

locators = Sauce_login()
data = Login_page_data()


class LoginPage(BasePage):
    username_field = (By.XPATH, '//input[@id="user-name"]')
    def login(self, username, password):
        self.url = data.main_page
        self.open()
        self.visibility_of_element_located(locators.username_field).send_keys(username)
        self.visibility_of_element_located(locators.password_field).send_keys(password)
        self.visibility_of_element_located(locators.login_button).click()

    def input_user_send_keys(self, text):
        self.find(self.username_field).send_keys(text)




