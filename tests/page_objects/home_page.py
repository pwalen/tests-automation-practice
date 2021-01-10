from tests.helpers.support_functions import *

your_logo = '//*[@id="header_logo"]/a/img'
sign_in_button = 'login'

def your_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, your_logo)
    return elem.is_displayed()

def go_to_authentication_page(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, sign_in_button)
    elem = driver_instance.find_element_by_id(sign_in_button)
    elem.click()




#! ============ DONE ============

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'

my_account_page_header_link = 'menu-item-100'
cart_page_header_link = 'menu-item-99'
add_hoodie_to_cart = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a'
go_to_cart_under_item = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a[2]'
cart_button_header = 'site-header-cart'



def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, taps_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_page_header_link)
    elem = driver_instance.find_element_by_id(my_account_page_header_link)
    elem.click()

#! ============ TO BE DONE ============

def add_item_to_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(add_hoodie_to_cart)
    elem.click()

def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, go_to_cart_under_item)
    elem1 = driver_instance.find_element_by_xpath(go_to_cart_under_item)
    elem1.click()