from tests.helpers.support_functions import *

first_slide_from_slider = '//*[@id="homeslider"]/li[2]/a/img'
sign_in_button = 'login'
women_button_from_top_menu = '//*[@id="block_top_menu"]/ul/li[1]/a'
# Faded Short Sleeve T-shirts
faded_short_tshirts = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img'

# Hovering over the "Faded Short Sleeve T-shirts" image, it displays the following elements:
quick_view_button = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[2]/span'
add_to_cart_button = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span'
more_button = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[2]/span'
faded_short_tshirts_name = '//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a'
faded_short_tshirts_price = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/div[2]/span'

# The popup "Product successfully added to your shopping cart" displays, with the image on the left.
popup_title = '//*[@id="layer_cart"]/div[1]/div[1]/h2/text()'
popup_title_text = "Product successfully added to your shopping cart"
# Next to the image, there are:
# the product name
faded_short_tshirts_name_on_popup = 'layer_cart_product_title'

# "Quantity" = 1
quantity = 'layer_cart_product_quantity'

# "Total" with the value equal to the product price.
total = 'layer_cart_product_price'

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


def hover_over_faded_short_tshirts(driver_instance):
    elem = driver_instance.find_element_by_xpath(faded_short_tshirts)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def quick_view_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, quick_view_button)
    return elem.is_displayed()


def add_to_cart_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, add_to_cart_button)
    return elem.is_displayed()


def more_button_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, more_button)
    return elem.is_displayed()


def faded_short_tshirts_name_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, faded_short_tshirts_name)
    return elem.is_displayed()

def faded_short_tshirts_price_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, faded_short_tshirts_price)
    return elem.is_displayed()

def click_add_to_cart_button(driver_instance):
    elem = driver_instance.find_element_by_xpath(add_to_cart_button)
    elem.click()


# The popup "Product successfully added to your shopping cart"
def popup_title_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, popup_title)
    return elem.is_displayed()


def popup_tittle_product_successfully_added(driver_instance):
    elem = driver_instance.find_element_by_xpath(popup_title)
    if elem.text == popup_title_text:
        return True
    else:
        return False


