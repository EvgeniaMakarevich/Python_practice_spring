from selenium.webdriver.common.by import By


class DragDropLocators:
    drag = (By.XPATH , "//div[@id = 'draggable']")
    drop = (By.XPATH, "//div[@id = 'droppable']")
    drag_drop_text =(By.XPATH, "//*[@id='droppable']/p[contains(text(),'Dropped')]")
