from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Python_practice_spring.lesson_1.Data.login_data import Login_page_data
from Python_practice_spring.lesson_1.Locators.login_locators import Sauce_login

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

data = Login_page_data()
locator = Sauce_login()


@pytest.fixture(scope='function')
def options():
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options


@pytest.fixture(scope='function')
def driver(options):
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get(data.main_page)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator.username_field)).send_keys(data.username)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator.password_field)).send_keys(data.password)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator.login_button)).click()
    yield driver
    driver.quit()
