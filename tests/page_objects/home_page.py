###* TC-REG: test_run/account_registration_test.py ###
###* TC-NAV: test_run/website_navigation_test.py ###

from tests.helpers.support_functions import *

# TC-NAV01 - 1. The site is accessible
# TC-NAV03 - 3. User is taken back to the home page
first_slide_from_slider = '//*[@id="homeslider"]/li[2]/a/img'

sign_in_button = 'login'

# TC-NAV02 - 2. Select WOMEN from the top menu
women_button_from_top_menu = '//*[@id="block_top_menu"]/ul/li[1]/a'

# TC-NAV04 - 3. Move the cursor over the image of the first product
faded_short_t_shirts = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img'

# TC-NAV04 - 3. The product's image will change to show either the second image containing
# the price, product name, and three buttons: "Quick view," "Add to cart," and "More."
faded_short_t_shirts_price = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/div[2]/span'
faded_short_t_shirts_name = '//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a'
quick_view_button = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[2]/span'
add_to_cart_button = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span'
more_button = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[2]/span'

# TC-NAV05 - 4. The popup "Product successfully added to your shopping cart" displays
popup_title_successfully_added = "Product successfully added to your shopping cart"

# TC-NAV05 - 4. (...) with the green checkmark on the left (...)
green_checkmark_on_popup = '//*[@id="layer_cart"]/div[1]/div[1]/h2/i'

# TC-NAV05 - 4. (...) Next to the checkmark, there are:
# a) the product name, the same as in the previous step (...)
faded_short_t_shirts_name_on_popup = 'layer_cart_product_title'

# TC-NAV05 - 4.  (...) b) "Quantity" equal to 1 (...)
quantity_on_popup = 'layer_cart_product_quantity'

# TC-NAV05 - 4. (...)  c) "Total" matching the product price shown previously (...)
total_on_popup = 'layer_cart_product_price'

# TC-NAV05 - 4. (...)  The right section of the popup is titled: "There is 1 item in your cart," (...)
right_section_title_on_popup = '//*[@id="layer_cart"]/div[1]/div[2]/h2/span[2]'
right_section_title_on_popup_message = "There is 1 item in your cart."


### *** *** *** *** ###

# TC-NAV01 - 1. The site is accessible
# TC-NAV03 - 3. User is taken back to the home page
def content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, first_slide_from_slider)
    return elem.is_displayed()


def go_to_authentication_page(driver_instance):
    wait_for_visibility_of_element_by_class_name(driver_instance, sign_in_button)
    elem = driver_instance.find_element_by_class_name(sign_in_button)
    elem.click()


# TC-NAV02 - Select WOMEN from the top menu
def click_women_button(driver_instance):
    elem = driver_instance.find_element_by_xpath(women_button_from_top_menu)
    elem.click()


# TC-NAV04 - 3. Move the cursor over the image of the first product
def hover_over_faded_short_tshirts(driver_instance):
    elem = driver_instance.find_element_by_xpath(faded_short_t_shirts)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


# TC-NAV04 - 3. (...) the price (...)
def faded_short_t_shirts_price_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, faded_short_t_shirts_price)
    return elem.is_displayed()


# TC-NAV04 - 3. (...) product name (...)
def faded_short_t_shirts_name_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, faded_short_t_shirts_name)
    return elem.is_displayed()


# TC-NAV04 - 3. (...) "Quick view"  (...)
def quick_view_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, quick_view_button)
    return elem.is_displayed()


# TC-NAV04 - 3. (...) "Add to cart" (...)
def add_to_cart_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, add_to_cart_button)
    return elem.is_displayed()


# TC-NAV04 - 3. (...) "More" (...)
def more_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, more_button)
    return elem.is_displayed()


# TC-NAV05 - Click the "Add to cart" button.
def click_add_to_cart_button(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, add_to_cart_button)
    elem.click()


# TC-NAV05 - 4. The popup "Product successfully added to your shopping cart" displays
def popup_tittle_product_successfully_added_displayed(driver_instance):
    if popup_title_successfully_added in driver_instance.page_source:
        return True
    else:
        return False


# TC-NAV05 - 4. (...) with the green checkmark on the left (...)
def green_checkmark_on_popup_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, green_checkmark_on_popup)
    return elem.is_displayed()


# TC-NAV05 - 4. (...) a) the product name corresponding with the name from the previous step (...)
def product_name_on_popup_the_same_as_on_hoover(driver_instance):
    product_name_on_popup_text = driver_instance.find_element_by_id(faded_short_t_shirts_name_on_popup).text
    product_name_on_hover = driver_instance.find_element_by_xpath(faded_short_t_shirts_name).text
    if product_name_on_popup_text == product_name_on_hover:
        return True
    else:
        return False


# TC-NAV05 - 4.  (...) b) "Quantity" equal to 1 (...)
def quantity_on_popup_equal_to_one(driver_instance):
    quantity_on_popup_text = driver_instance.find_element_by_id(quantity_on_popup).text
    if quantity_on_popup_text == "1":
        return True
    else:
        return False


# TC-NAV05 - 4. (...)  c) "Total" matching the product price shown previously (...)
def total_matching_product_price(driver_instance):
    faded_short_t_shirts_price_text = wait_for_visibility_of_element_by_xpath(driver_instance,
                                                                              faded_short_t_shirts_price)
    total_on_popup_text = wait_for_visibility_of_element_by_xpath(driver_instance, total_on_popup)
    if faded_short_t_shirts_price_text == total_on_popup_text:
        return True
    else:
        return False


# TC-NAV05 - 4. (...) The right section of the popup is titled: "There is 1 item in your cart," (...)
def correct_right_section_title_on_popup(driver_instance):
    right_section_title_on_popup_text = driver_instance.find_element_by_xpath(right_section_title_on_popup).text
    if right_section_title_on_popup_text == right_section_title_on_popup_message:
        return True
    else:
        return False
