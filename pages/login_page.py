from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        register_form_for_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_FOR_EMAIL)
        register_form_for_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_FOR_PASSWORD)
        register_form_for_password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_FOR_PASSWORD_2)
        register_form_btn = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BTN)
        register_form_for_email.send_keys(email)
        register_form_for_password.send_keys(password)
        register_form_for_password_2.send_keys(password)
        register_form_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
    	assert 'login' in self.url, "login is absent in current url"

    def should_be_login_form(self):
    	assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
    	assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
