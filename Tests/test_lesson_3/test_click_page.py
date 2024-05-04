import time

from lesson_3.Pages.Click_page import ClickPage
from lesson_3.Locators.Click_locators import ClickLocators
class TestButton:
    locators = ClickLocators()
    def test_double_click(self, driver):
        test = ClickPage()
        driver.get('https://demoqa.com/buttons')
        test.double_click(driver, self.locators.double_click)
        success_text = driver.find_element(*self.locators.double_click_text)
        assert success_text.is_displayed()


    def test_right_click(self, driver):
        test = ClickPage()
        driver.get('https://demoqa.com/buttons')
        test.right_click(driver, self.locators.right_click)
        time.sleep(3)



