from features.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    your_account_has_been_created_header_xpath = "//div[@id='content']/h1"

    def display_status_of_your_account_has_been_created_header(self, message):
        return self.display_status("your_account_has_been_created_header_xpath", self.your_account_has_been_created_header_xpath)
