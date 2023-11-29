import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given(u'the user is on the login page')
def step_impl(context):
    utils.set_driver_config(context)
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.login_page = context.home_page.click_on_login_option()


@when(u'the user enters the email as \'y2k@y2k.com\'')
def step_impl(context):
    context.login_page.enter_email('y2k@y2k.com')


@when(u'the user enters the password as \'1234\'')
def step_impl(context):
    context.login_page.enter_password('1234')


@when(u'the user clicks on the login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()


@then(u'the user is logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(u'the user enters the email as \'\'')
def step_impl(context):
    context.login_page.enter_email('')


@when(u'the user enters the password as \'\'')
def step_impl(context):
    context.login_page.enter_password('')


@then(u'a \'Warning: No match for E-Mail Address and/or Password.\' is displayed')
def step_impl(context):
    assert context.login_page.display_status_of_warning_message('Warning: No match for E-Mail Address and/or Password.')
    utils.quit_driver(context)
