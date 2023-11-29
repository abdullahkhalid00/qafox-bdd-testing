import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given(u'the user is on the home page')
def step_impl(context):
    utils.set_driver_config(context)


@when(u'the user enters a valid product as \'HP LP3065\'')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('HP LP3065')


@when(u'the user clicks on the search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_the_search_button()


@then(u'the valid product \'HP LP3065\' is displayed')
def step_impl(context):
    assert context.search_page.display_status_of_valid_product('HP LP3065')


@when(u'the user enters a valid product as \'Samsung Galaxy Tab 10.1\'')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('Samsung Galaxy Tab 10.1')


@then(u'the valid product \'Samsung Galaxy Tab 10.1\' is displayed')
def step_impl(context):
    assert context.search_page.display_status_of_valid_product('Samsung Galaxy Tab 10.1')


@when(u'the user enters a valid product as \'iPhone\'')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('iPhone')


@then(u'the valid product \'iPhone\' is displayed')
def step_impl(context):
    assert context.search_page.display_status_of_valid_product('iPhone')


@when(u'the user enters an invalid product')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('Dell')


@when(u'the user leaves the search box blank')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_a_product_into_the_search_box('')


@then(u'a proper warning message is displayed')
def step_impl(context):
    assert context.search_page.display_status_of_warning_message('There is no product that matches the search criteria.')
    utils.quit_driver(context)
