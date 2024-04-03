from selenium.webdriver.common.by import By


class FiltrationLocators:
    filtration_dropdown = (By.XPATH, "//select[@data-test = 'product-sort-container']")