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

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def visibility_of_element_located(self, locator):
        wait = self.wait()
        return wait.until(EC.visibility_of_element_located(locator))
    def clickability_of_element_located(self, locator):
        wait = self.wait()
        return wait.until(EC.element_to_be_clickable(locator))

    def visibility_of_element_not_located(self,locator):
        wait = self.wait()
        return wait.until_not(EC.visibility_of_element_located(locator))

    def find(self, element):
        return self.driver.find_element(*element)

    def element_is_displayed(self, locator):
        wait = self.wait()
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def get_text(self, locator):
        wait = self.wait()
        text = wait.until(EC.visibility_of_element_located(locator)).text
        return text
