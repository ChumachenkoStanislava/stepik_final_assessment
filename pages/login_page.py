from .base_page import BasePage
from .locators import MainPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        self.is_element_present(*MainPageLocators.login_form), "Login form is not presented"


    def should_be_register_form(self):
        self.is_element_present(*MainPageLocators.register_form), "Register form is not presented"
