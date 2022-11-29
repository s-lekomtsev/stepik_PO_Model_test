from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес driver.current_url
        assert self.browser.current_url.find("login") != -1, "Login is not presented in URL"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)

        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        input_password1.send_keys(password)

        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        input_password2.send_keys(password)

        btn_login = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        btn_login.click()

