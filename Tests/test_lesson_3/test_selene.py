import time
from lesson_3.Pages.Auth_page import AuthPage, browser_management
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s,ss

url = 'https://victoretc.github.io/selenium_waits/'
class TestAuth:
    def test_auth(self, browser_management):
        auth = AuthPage()
        auth.visit(url)
        auth.start()
        auth.login()
        auth.success_message_have_text('Вы успешно зарегистрированы!')

