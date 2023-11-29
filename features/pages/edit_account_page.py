from features.pages.base_page import BasePage


class EditAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_input_field_id = 'input-email'
    continue_button_xpath = "//div[@class='pull-right']/input"
    email_address_already_registered_text_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_new_email(self, email):
        self.type_into_element("email_input_field_id", self.email_input_field_id, email)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)

    def display_status_of_email_address_already_registered_text_message(self):
        return self.display_status("email_address_already_registered_text_xpath", self.email_address_already_registered_text_xpath)