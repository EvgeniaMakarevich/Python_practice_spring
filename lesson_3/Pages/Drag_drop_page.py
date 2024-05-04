from selenium.webdriver import ActionChains
from lesson_3.Locators.Drag_drop_locators import DragDropLocators


class DragDrop:
    locators = DragDropLocators()

    def drag_and_drop(self, driver, drag_locator, drop_locator):
        action = ActionChains(driver)
        drag = driver.find_element(*drag_locator)
        drop = driver.find_element(*drop_locator)
        drag_drop = action.drag_and_drop(drag, drop)
        drag_drop.perform()
