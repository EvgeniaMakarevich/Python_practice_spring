from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print(f"An error occurred while opening the page: {e}")

    def visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def visibility_of_element_not_located(self,locator):
        return WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(locator))
