from selenium.webdriver import ActionChains



class ClickPage:

    def double_click(self, driver, element):
        action = ActionChains(driver)
        item = driver.find_element(*element)
        return action.double_click(item).perform()

    def right_click(self, driver, element):
        action = ActionChains(driver)
        item = driver.find_element(*element)
        return action.context_click(item).perform()
