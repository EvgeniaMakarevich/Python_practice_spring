from selene import browser, by, be, have
from selene.support.shared.jquery_style import s,ss

browser.config.window_width = 100
browser.config.window_height = 500

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

