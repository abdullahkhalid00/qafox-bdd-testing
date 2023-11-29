from features.pages.base_page import BasePage
from features.pages.change_password_page import ChangePasswordPage
from features.pages.edit_account_page import EditAccountPage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_information_option_link_text = 'Edit your account information'
    change_your_password_link_text = 'Change your password'
    your_account_has_been_successfully_updated_text_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def display_status_of_edit_your_account_information_option(self):
        return self.display_status("edit_your_account_information_option_link_text", self.edit_your_account_information_option_link_text)

    def click_on_change_your_password_option(self):
        self.click_on_element("change_your_password_link_text", self.change_your_password_link_text)
        return ChangePasswordPage(self.driver)

    def click_on_edit_your_account_information_option(self):
        self.click_on_element("edit_your_account_information_option_link_text", self.edit_your_account_information_option_link_text)
        return EditAccountPage(self.driver)

    def display_status_of_your_account_has_been_successfully_updated_text_message(self):
        return self.display_status("your_account_has_been_successfully_updated_text_xpath", self.your_account_has_been_successfully_updated_text_xpath)
