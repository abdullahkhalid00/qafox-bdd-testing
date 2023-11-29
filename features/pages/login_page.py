from selenium.webdriver.common.by import By
from features.pages.account_page import AccountPage
from features.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email(self, email):
        self.type_into_element("email_field_id", self.email_field_id, email)

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def display_status_of_warning_message(self, warning_message):
        return self.retrieved_element_text_contains("warning_message_xpath", self.warning_message_xpath, warning_message)
