###* TC-NAV: test_run/website_navigation_test.py ###

from tests.helpers.support_functions import *

# TC-NAV02 - 2. The user is redirected to the category page for Woman. The banner titled "Woman" is visible.
category_name_on_banner = "category-name"

# TC-NAV03 - 3. Click Your Logo
logo = '//*[@id="header_logo"]/a/img'


# TC-NAV02 - 2. The user is redirected to the category page for Woman. The banner titled "Woman" is visible.
def woman_on_banner_visible(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, category_name_on_banner)
    elem = driver_instance.find_element_by_class_name(category_name_on_banner)
    # elem = driver_instance.find_element_by_class_name(category_name_on_banner)
    if elem.text == "Women":
        return True
    else:
        return False


# TC-NAV03 - 3. Click Your Logo
def click_logo(driver_instance):
    elem = driver_instance.find_element_by_xpath(logo)
    elem.click()
