from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_texts = ["HP LP3065", "Samsung Galaxy Tab 10.1", "iPhone"]
    warning_message_xpath = "//*[@id='content']/p[2]"

    def display_status_of_valid_product(self, productname):
        if productname in self.valid_product_link_texts:
            return self.display_status("valid_product_link_text", productname)

    def display_status_of_warning_message(self, warning_message):
        return self.retrieved_element_text_equals("warning_message_xpath", self.warning_message_xpath, warning_message)
