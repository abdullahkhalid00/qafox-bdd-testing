from datetime import datetime

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'the user is on the registration page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, "//*[@id='top-links']/ul/li[2]/a").click()
    context.driver.find_element(By.LINK_TEXT, 'Register').click()


@when(u'the user enters the firstname as \'ABC\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('ABC')


@when(u'the user enters the lastname as \'XYZ\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-lastname').send_keys('XYZ')


@when("the user enters the email")
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    context.driver.find_element(By.ID, 'input-email').send_keys('abc' + time_stamp + '@abc.com')


@when(u'the user enters the telephone number as \'12345\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-telephone').send_keys('12345')


@when(u'the user enters the password as \'ABCXYZ\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-password').send_keys('ABCXYZ')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('ABCXYZ')


@when(u'the user checks the privacy policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, 'agree').click()


@when(u'the user clicks on the continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then("the user is registered")
def step_impl(context):
    expected_output = 'Your Account Has Been Created!'
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_output)


@then(u'a \'Warning: E-Mail Address is already registered!\' is displayed')
def step_impl(context):
    warning_message = 'Warning: E-Mail Address is already registered!'
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__eq__(warning_message)


@when(u'the user enters the firstname as \'\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('')


@when(u'the user enters the lastname as \'\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-lastname').send_keys('')


@when(u'the user enters the telephone number as \'1\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-telephone').send_keys('1')


@then(u'a \'Telephone must be between 3 and 32 characters!\' is displayed')
def step_impl(context):
    telephone_warning_message = 'Telephone must be between 3 and 32 characters!'
    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(telephone_warning_message)


@when(u'the user enters the telephone number as \'\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-telephone').send_keys('')


@when(u'the user enters the password as \'ABC\'')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-password').send_keys('ABC')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('ABC')


@then(u'a \'Password must be between 4 and 20 characters!\' is displayed')
def step_impl(context):
    password_warning_message = 'Password must be between 4 and 20 characters!'
    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(password_warning_message)


@when("the user leaves every field blank")
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('')
    context.driver.find_element(By.ID, 'input-email').send_keys('')
    context.driver.find_element(By.ID, 'input-telephone').send_keys('')
    context.driver.find_element(By.ID, 'input-password').send_keys('')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('')


@then("a proper warning message for each field is displayed")
def step_impl(context):
    privacy_policy_warning_message = 'Warning: You must agree to the Privacy Policy!'
    first_name_warning_message = 'First Name must be between 1 and 32 characters!'
    last_name_warning_message = 'Last Name must be between 1 and 32 characters!'
    email_warning_message = 'E-Mail Address does not appear to be valid!'
    telephone_warning_message = 'Telephone must be between 3 and 32 characters!'
    password_warning_message = 'Password must be between 4 and 20 characters!'
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(privacy_policy_warning_message)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(first_name_warning_message)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(last_name_warning_message)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(email_warning_message)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(telephone_warning_message)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(password_warning_message)
    context.driver.quit()
