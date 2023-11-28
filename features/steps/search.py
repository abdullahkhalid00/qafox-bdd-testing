from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'the user is on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')


@when(u'the user enters a valid product as \'HP LP3065\'')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('HP LP3065')


@when(u'the user clicks on the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then(u'the valid product \'HP LP3065\' is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()


@when(u'the user enters a valid product as \'Samsung Galaxy Tab 10.1\'')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Samsung Galaxy Tab 10.1')


@then(u'the valid product \'Samsung Galaxy Tab 10.1\' is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'Samsung Galaxy Tab 10.1').is_displayed()


@when(u'the user enters a valid product as \'iPhone\'')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('iPhone')


@then(u'the valid product \'iPhone\' is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'iPhone').is_displayed()


@when(u'the user enters an invalid product')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Samsung Galaxy s23')


@when(u'the user leaves the search box blank')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('')


@then(u'a proper warning message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//*[@id='content']/p[2]").is_displayed()
    context.driver.quit()
