import pytest
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s,ss
from selenium import webdriver

browser.config.window_width = 100
browser.config.window_height = 500

@pytest.fixture
def browser_management(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless=new')
    options.add_argument("--lang=en")
    browser.config.driver_options = options

    browser.config.timeout = 3

    yield browser

    browser.quit()

class AuthPage:
    def visit(self, url):
        browser.open(url)

    def start(self):
        return browser.element(by.xpath('//*[@id="startTest"]')).with_(timeout = 10).click()

    def login(self):
        s('#login').type('login')
        s('#password').type('password')
        s('#agree').click()
        browser.element(by.text('Зарегистрироваться')).click()

    def success_message_have_text(self, text):
        s('#successMessage').should(have.text(text))

