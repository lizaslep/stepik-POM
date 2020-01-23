from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        strn = "login" in url
        assert strn == True, "It's a wrong url."

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "No email field in the login form!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "No password field in the login form!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "No email field in the registration form!"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_FIELD), "No password fiels in the registration form!"
        assert self.is_element_present(*LoginPageLocators.REG_REP_PASSWORD_FIELD), "No repeat password fiels in the registration form!"