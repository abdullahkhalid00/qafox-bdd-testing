import utils
from features.pages.account_created_page import AccountCreatedPage
from features.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    email_address_already_registered_text_xpath = "//div[@id='account-register']/div[1]"
    telephone_number_must_be_between_3_and_32_characters_text_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_must_be_between_4_and_20_characters_text_xpath = "//input[@id='input-password']/following-sibling::div"
    you_must_agree_to_the_privacy_policy_text_xpath = "//div[@id='account-register']/div[1]"
    first_name_must_be_between_1_and_32_characters_text_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_must_be_between_1_and_32_characters_text_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_does_not_appear_to_be_valid_text_xpath = "//input[@id='input-email']/following-sibling::div"

    def enter_first_name(self, fname):
        self.type_into_element("first_name_field_id", self.first_name_field_id, fname)

    def enter_last_name(self, lname):
        self.type_into_element("last_name_field_id", self.last_name_field_id, lname)

    def enter_email(self):
        self.type_into_element("email_field_id", self.email_field_id, utils.get_new_email_with_timestamp())

    def leave_email_blank(self):
        self.type_into_element("email_field_id", self.email_field_id, "")

    def enter_duplicate_email(self, email):
        self.type_into_element("email_field_id", self.email_field_id, email)

    def enter_telephone(self, telephone):
        self.type_into_element("telephone_field_id", self.telephone_field_id, telephone)

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def confirm_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def check_privacy_policy_option(self):
        self.click_on_element("privacy_policy_option_name", self.privacy_policy_option_name)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountCreatedPage(self.driver)

    def display_status_of_email_address_already_registered_text_message(self, message):
        return self.retrieved_element_text_equals("email_address_already_registered_text_xpath", self.email_address_already_registered_text_xpath, message)

    def display_status_of_telephone_number_must_be_between_3_and_32_characters_text_message(self, message):
        return self.retrieved_element_text_equals("telephone_number_must_be_between_3_and_32_characters_text_xpath", self.telephone_number_must_be_between_3_and_32_characters_text_xpath, message)

    def display_status_of_password_must_be_between_4_and_20_characters_text_message(self, message):
        return self.retrieved_element_text_equals("password_must_be_between_4_and_20_characters_text_xpath", self.password_must_be_between_4_and_20_characters_text_xpath, message)

    def display_status_of_you_must_agree_to_the_privacy_policy_text_message(self, message):
        return self.retrieved_element_text_equals("you_must_agree_to_the_privacy_policy_text_xpath", self.you_must_agree_to_the_privacy_policy_text_xpath, message)

    def display_status_of_first_name_must_be_between_1_and_32_characters_text_message(self, message):
        return self.retrieved_element_text_equals("first_name_must_be_between_1_and_32_characters_text_xpath", self.first_name_must_be_between_1_and_32_characters_text_xpath, message)

    def display_status_of_last_name_must_be_between_1_and_32_characters_text_message(self, message):
        return self.retrieved_element_text_equals("last_name_must_be_between_1_and_32_characters_text_xpath", self.last_name_must_be_between_1_and_32_characters_text_xpath, message)

    def display_status_of_email_does_not_appear_to_be_valid_text_message(self, message):
        return self.retrieved_element_text_equals("email_does_not_appear_to_be_valid_text_xpath", self.email_does_not_appear_to_be_valid_text_xpath, message)
