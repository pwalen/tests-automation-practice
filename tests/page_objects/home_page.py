from tests.helpers.support_functions import *

home_page_content = 'columns'
sign_in_button = 'login'


def home_page_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, home_page_content)
    return elem.is_displayed()


def go_to_authentication_page(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, sign_in_button)
    elem = driver_instance.find_element_by_class_name(sign_in_button)
    elem.click()
