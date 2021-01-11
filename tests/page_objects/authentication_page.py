from tests.helpers.support_functions import *
from faker import Faker

authentication_header = '//*[@id="center_column"]/h1'
email_registration_field = 'email_create'
create_account_button = 'SubmitCreate'
proper_email = Faker().ascii_email()


def my_account_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, authentication_header)
    return elem.is_displayed()


def correct_email_submission(driver_instance):
    elem = driver_instance.find_element_by_id(email_registration_field)
    elem.send_keys(proper_email)


def click_create_account_button(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, create_account_button)
    elem.click()
