from selenium.webdriver.common.by import By


class ClickLocators:
    double_click = (By.XPATH, "//button[@id = 'doubleClickBtn']")
    right_click = (By.XPATH,"//button[@id = 'rightClickBtn']")
    double_click_text = (By.XPATH, "//p[@id ='doubleClickMessage']")
