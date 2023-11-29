import utils
from behave import given, when, then
from features.pages.home_page import HomePage


@given(u'the user is on the registration page')
def step_impl(context):
    utils.set_driver_config(context)
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.register_page = context.home_page.click_on_register_option()


@when(u'the user enters the firstname as \'ABC\'')
def step_impl(context):
    context.register_page.enter_first_name('ABC')


@when(u'the user enters the lastname as \'XYZ\'')
def step_impl(context):
    context.register_page.enter_last_name('XYZ')


@when("the user enters the email")
def step_impl(context):
    context.register_page.enter_email()


@when(u'the user enters the telephone number as \'12345\'')
def step_impl(context):
    context.register_page.enter_telephone('12345')


@when(u'the user enters the password as \'ABCXYZ\'')
def step_impl(context):
    context.register_page.enter_password('ABCXYZ')
    context.register_page.confirm_password('ABCXYZ')


@when(u'the user checks the privacy policy option')
def step_impl(context):
    context.register_page.check_privacy_policy_option()


@when(u'the user clicks on the continue button')
def step_impl(context):
    context.account_created_page = context.register_page.click_on_continue_button()


@then("the user is registered")
def step_impl(context):
    assert context.account_created_page.display_status_of_your_account_has_been_created_header('Your Account Has Been Created!')


@when(u'the user enters the registration email as \'\'')
def step_impl(context):
    context.register_page.leave_email_blank()


@when(u'the user enters the registration email as \'y2k@y2k.com\'')
def step_impl(context):
    context.register_page.enter_duplicate_email('y2k@y2k.com')


@when(u'the user enters the registration password as \'\'')
def step_impl(context):
    context.register_page.enter_password('')


@then(u'a \'Warning: E-Mail Address is already registered!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_email_address_already_registered_text_message('Warning: E-Mail Address is already registered!')


@when(u'the user enters the firstname as \'\'')
def step_impl(context):
    context.register_page.enter_first_name('')


@when(u'the user enters the lastname as \'\'')
def step_impl(context):
    context.register_page.enter_last_name('')


@when(u'the user enters the telephone number as \'1\'')
def step_impl(context):
    context.register_page.enter_telephone('1')


@then(u'a \'Telephone must be between 3 and 32 characters!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_telephone_number_must_be_between_3_and_32_characters_text_message('Telephone must be between 3 and 32 characters!')


@when(u'the user enters the telephone number as \'\'')
def step_impl(context):
    context.register_page.enter_telephone('')


@when(u'the user enters the registration password as \'ABCXYZ\'')
def step_impl(context):
    context.register_page.enter_password('ABCXYZ')
    context.register_page.confirm_password('ABCXYZ')


@when(u'the user enters the registration password as \'ABC\'')
def step_impl(context):
    context.register_page.enter_password('ABC')
    context.register_page.confirm_password('ABC')


@then(u'a \'Password must be between 4 and 20 characters!\' is displayed')
def step_impl(context):
    assert context.register_page.display_status_of_password_must_be_between_4_and_20_characters_text_message('Password must be between 4 and 20 characters!')


@when("the user leaves every field blank")
def step_impl(context):
    context.register_page.enter_first_name('')
    context.register_page.enter_last_name('')
    context.register_page.leave_email_blank()
    context.register_page.enter_telephone('')
    context.register_page.enter_password('')
    context.register_page.confirm_password('')


@then("a proper warning message for each field is displayed")
def step_impl(context):
    privacy_policy_warning_message = 'Warning: You must agree to the Privacy Policy!'
    first_name_warning_message = 'First Name must be between 1 and 32 characters!'
    last_name_warning_message = 'Last Name must be between 1 and 32 characters!'
    email_warning_message = 'E-Mail Address does not appear to be valid!'
    telephone_warning_message = 'Telephone must be between 3 and 32 characters!'
    password_warning_message = 'Password must be between 4 and 20 characters!'
    assert context.register_page.display_status_of_you_must_agree_to_the_privacy_policy_text_message(privacy_policy_warning_message)
    assert context.register_page.display_status_of_first_name_must_be_between_1_and_32_characters_text_message(first_name_warning_message)
    assert context.register_page.display_status_of_last_name_must_be_between_1_and_32_characters_text_message(last_name_warning_message)
    assert context.register_page.display_status_of_email_does_not_appear_to_be_valid_text_message(email_warning_message)
    assert context.register_page.display_status_of_telephone_number_must_be_between_3_and_32_characters_text_message(telephone_warning_message)
    assert context.register_page.display_status_of_password_must_be_between_4_and_20_characters_text_message(password_warning_message)
    utils.quit_driver(context)
