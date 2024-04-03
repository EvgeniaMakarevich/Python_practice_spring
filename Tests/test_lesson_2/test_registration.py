from selenium.webdriver.common.by import By
from faker import Faker
from conftest import driver

fake = Faker()

def test_registration_with_checkbox(driver):
    driver.get('https://victoretc.github.io/webelements_information/')
    username = fake.first_name()
    driver.find_element(By.XPATH, "//input[@id = 'username']").send_keys(username)
    registration_button = driver.find_element(By.XPATH, "//button[@id = 'registerButton']")
    assert not registration_button.is_enabled()

    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys(password)
    assert not registration_button.is_enabled()

    checkbox = driver.find_element(By.XPATH, "//input[@id = 'agreement']")
    checkbox.click()
    assert checkbox.is_selected()
    assert registration_button.is_enabled()

