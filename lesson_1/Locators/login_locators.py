from selenium.webdriver.common.by import By


class Sauce_login:
    username_field = (By.XPATH, "//input[@data-test = 'username']")
    password_field = (By.XPATH, "//input[@data-test = 'password']")
    login_button = (By.XPATH, "//input[@data-test = 'login-button']")
    wrong_container = (By.XPATH, "//div[@class = 'error-message-container error']")
    login_interface = (By.XPATH, "//div[@class = 'login_wrapper']")