from tests.helpers.support_functions import *
import random
import datetime
import string
from faker import Faker
from calendar import monthrange


account_creation_form = 'account-creation_form'
radio_button_mr = 'id_gender1'
radio_button_mrs = 'id_gender2'
firstname_field1 = 'customer_firstname'
lastname_field1 = 'customer_lastname'
password_field = 'passwd'
dropdown_days = 'days'
dropdown_months = 'months'
dropdown_years = 'years'
checkbox_newsletter = 'newsletter'
checkbox_special_offers = 'optin'
firstname_field2 = 'firstname'
lastname_field2 = 'lastname'
address_field1 = 'address1'
city_field = 'city'
dropdown_states = 'id_state'
postcode_field = 'postcode'
phone_mobile_field = 'phone_mobile'
alias_field = 'alias'
register_button = 'submitAccount'

state_index_dictionary = {'Alabama': 1, 'Alaska': 2, 'Arizona': 3, 'Arkansas': 4, 'California': 5, 'Colorado': 6,
                          'Connecticut': 7, 'Delaware': 8, 'District of Columbia': 9, 'Florida': 10, 'Georgia': 11,
                          'Hawaii': 12, 'Idaho': 13, 'Illinois': 14, 'Indiana': 15, 'Iowa': 16, 'Kansas': 17,
                          'Kentucky': 18, 'Louisiana': 19, 'Maine': 20, 'Maryland': 21, 'Massachusetts': 22,
                          'Michigan': 23, 'Minnesota': 24, 'Mississippi': 25, 'Missouri': 26, 'Montana': 27,
                          'Nebraska': 28, 'Nevada': 29, 'New Hampshire': 30, 'New Jersey': 31, 'New Mexico': 32,
                          'New York': 33, 'North Carolina': 34, 'North Dakota': 35, 'Ohio': 36, 'Oklahoma': 37,
                          'Oregon': 38, 'Pennsylvania': 39, 'Puerto Rico': 40, 'Rhode Island': 41, 'South Carolina': 42,
                          'South Dakota': 43, 'Tennessee': 44, 'Texas': 45, 'US Virgin Islands': 46, 'Utah': 47,
                          'Vermont': 48, 'Virginia': 49, 'Washington': 50, 'West Virginia': 51, 'Wisconsin': 52,
                          'Wyoming': 53}



def random_characters(y):
    return ''.join(random.choice(string.ascii_letters) for _x in range(y))


firstname = Faker().first_name()
lastname = Faker().last_name()
password = Faker().password(10)
street_address = Faker().street_address()
city = Faker().city()
states_tuple = tuple(state_index_dictionary.keys())
state = random.choice(states_tuple)
postcode = Faker().postalcode()
phone_mobile = Faker().random_number(10)
alias = random_characters(5).lower()

year_of_birth = random.randint(1900, 2003)
month_of_birth = random.randint(1, 13)
days_in_birth_month = monthrange(year_of_birth, month_of_birth)
day_of_birth = random.randint(1, days_in_birth_month[1] + 1)


def account_creation_form_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, account_creation_form)
    elem = driver_instance.find_element_by_id(account_creation_form)
    return elem.is_displayed()


def radio_button_mr_selection(driver_instance):
    elem = driver_instance.find_element_by_id(radio_button_mr)
    elem.click()


def radio_button_mrs_selection(driver_instance):
    elem = driver_instance.find_element_by_id(radio_button_mrs)
    elem.click()


def correct_firstname1_submission(driver_instance):
    elem = driver_instance.find_element_by_id(firstname_field1)
    elem.send_keys(firstname)


def correct_lastname1_submission(driver_instance):
    elem = driver_instance.find_element_by_id(lastname_field1)
    elem.send_keys(lastname)


def correct_password_submission(driver_instance):
    elem = driver_instance.find_element_by_id(password_field)
    elem.send_keys(password)


def convert_year_to_dropdown_index(year):
    current_year = datetime.datetime.now().year
    years = list(range(current_year, current_year - 123, -1))
    corresponding_indexes = list(range(1, 123))
    zip_iterator = zip(years, corresponding_indexes)
    year_index_dictionary = dict(zip_iterator)
    return year_index_dictionary[year]


def correct_birth_year_selection(driver_instance):
    elem = Select(driver_instance.find_element_by_id(dropdown_years))
    elem.select_by_index(convert_year_to_dropdown_index(year_of_birth))


def correct_birth_month_selection(driver_instance):
    elem = Select(driver_instance.find_element_by_id(dropdown_months))
    elem.select_by_index(month_of_birth)


def correct_birth_day_selection(driver_instance):
    elem = Select(driver_instance.find_element_by_id(dropdown_days))
    elem.select_by_index(day_of_birth)


def checkbox_newsletter_selection(driver_instance):
    elem = driver_instance.find_element_by_id(checkbox_newsletter)
    elem.click()


def checkbox_special_offers_selection(driver_instance):
    elem = driver_instance.find_element_by_id(checkbox_special_offers)
    elem.click()


def correct_firstname2_submission(driver_instance):
    elem = driver_instance.find_element_by_id(firstname_field2)
    elem.send_keys(firstname)


def correct_lastname2_submission(driver_instance):
    elem = driver_instance.find_element_by_id(lastname_field2)
    elem.send_keys(lastname)


def correct_address1_submission(driver_instance):
    elem = driver_instance.find_element_by_id(address_field1)
    elem.send_keys(street_address)


def correct_city_submission(driver_instance):
    elem = driver_instance.find_element_by_id(city_field)
    elem.send_keys(city)


def correct_state_selection(driver_instance):
    elem = Select(driver_instance.find_element_by_id(dropdown_states))
    elem.select_by_index(state_index_dictionary[state])


def correct_postcode_submission(driver_instance):
    elem = driver_instance.find_element_by_id(postcode_field)
    elem.send_keys(postcode)


def correct_phone_mobile_submission(driver_instance):
    elem = driver_instance.find_element_by_id(phone_mobile_field)
    elem.send_keys(phone_mobile)


def correct_alias_submission(driver_instance):
    elem = driver_instance.find_element_by_id(alias_field)
    elem.send_keys(alias)


def register_button_click(driver_instance):
    elem = driver_instance.find_element_by_id(register_button)
    elem.click()

