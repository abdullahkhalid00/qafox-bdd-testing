from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage
from features.pages.search_page import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//*[@id='top-links']/ul/li[2]/a"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account_option(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def click_on_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)

    def enter_a_product_into_the_search_box(self, productname):
        self.type_into_element("search_box_field_name", self.search_box_field_name, productname)

    def click_on_the_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
