from tests.helpers.support_functions import *

welcome_message = 'Welcome to your account. Here you can manage all of your personal information and orders.'
account_center_column = 'center_column'
logout_button = 'logout'


def account_center_column_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, account_center_column)
    elem = driver_instance.find_element_by_id(account_center_column)
    elem.is_displayed()


def welcome_message_displayed(driver_instance):
    if welcome_message in driver_instance.page_source:
        return True
    else:
        return False


def logout_button_click(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, logout_button)
    elem = driver_instance.find_element_by_class_name(logout_button)
    elem.click()