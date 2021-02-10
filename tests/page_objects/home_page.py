from tests.helpers.support_functions import *

first_slide_from_slider = '//*[@id="homeslider"]/li[2]/a/img'
sign_in_button = 'login'
women_button_from_top_menu = '//*[@id="block_top_menu"]/ul/li[1]/a'


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, first_slide_from_slider)
    return elem.is_displayed()


def go_to_authentication_page(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, sign_in_button)
    elem = driver_instance.find_element_by_class_name(sign_in_button)
    elem.click()


def click_women_button(driver_instance):
    elem = driver_instance.find_element_by_xpath(women_button_from_top_menu)
    elem.click()

