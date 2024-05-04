# import time
#
# from lesson_3.Pages.Drag_drop_page import DragDrop
# from lesson_3.Locators.Drag_drop_locators import DragDropLocators
# class TestDragDrop:
#     locators = DragDropLocators()
#     def test_drag_drop(self, driver):
#         test = DragDrop()
#         driver.get('https://demoqa.com/droppable')
#         test.drag_and_drop(driver, self.locators.drag, self.locators.drop)
#         text = driver.find_element(*self.locators.drag_drop_text).text
#         assert text == 'Dropped!'
#         time.sleep(3)
