from tests.helpers.support_functions import *

category_name_on_banner = "category-name"
logo = '//*[@id="header_logo"]/a/img'


def woman_on_banner_visible(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, category_name_on_banner)
    elem = driver_instance.find_element_by_class_name(category_name_on_banner)
    # elem = driver_instance.find_element_by_class_name(category_name_on_banner)
    if elem.text == "Women":
        return True
    else:
        return False


def click_logo(driver_instance):
    elem = driver_instance.find_element_by_xpath(logo)
    elem.click()
