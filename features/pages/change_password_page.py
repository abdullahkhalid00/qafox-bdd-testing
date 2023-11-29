from features.pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    password_field_id = 'input-password'
    confirm_password_field_id = 'input-confirm'
    continue_button_xpath = "//div[@class='pull-right']//input"

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def confirm_password(self, password):
        self.type_into_element("confirm_password_field_id", self.confirm_password_field_id, password)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
