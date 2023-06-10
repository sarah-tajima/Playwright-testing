from Automationtests.src.pages.LandingPage import LandingPage

class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("#gigya-login-form input[name=\"username\"]")
        self._password = page.locator("#gigya-login-form input[name=\"password\"]")
        self._login_btn =  page.get_by_role("button", name="Log In")
        self._invalid_message = page.get_by_text("Invalid User ID or password")

    def enter_username(self, username):
        self._username.fill(username)

    def enter_password(self, password):
        self._password.fill(password)

    def click_login(self):
         self._login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return LandingPage(self.page)

    @property
    def err_msg_loc(self):
        return self._invalid_message