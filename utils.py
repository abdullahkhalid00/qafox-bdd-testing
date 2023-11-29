from datetime import datetime

from selenium import webdriver

URL = 'https://tutorialsninja.com/demo/'


def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "abc" + time_stamp + "@abc.com"


def set_driver_config(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(URL)

    return context.driver


def quit_driver(context):
    context.driver.quit()
