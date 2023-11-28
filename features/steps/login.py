from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, "//*[@id='top-links']/ul/li[2]/a").click()
    context.driver.find_element(By.LINK_TEXT, 'Login').click()


@when(u'the user enters the email as \'y2k@y2k.com\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('y2k@y2k.com')


@when(u'the user enters the password as \'1234\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-password').send_keys('1234')


@when(u'the user clicks on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div/form/input").click()


@then(u'the user is logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'Edit your account information').is_displayed()


@when(u'the user enters the email as \'\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('')


@when(u'the user enters the password as \'\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-password').send_keys('')


@then(u'a \'Warning: No match for E-Mail Address and/or Password.\' is displayed')
def step_impl(context):
    warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__eq__(warning_message)
    context.driver.quit()
