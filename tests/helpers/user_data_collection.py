from csv import writer
from tests.page_objects.account_creation_page import firstname, lastname, password, date_of_birth, street_address, \
    city, state, postcode, phone_mobile, alias
from tests.page_objects.authentication_page import proper_email

user_data = [proper_email, password, firstname, lastname, date_of_birth, street_address, city, state, postcode,
             phone_mobile, alias]


def export_user_data_to_csv():
    with open('user_data.csv', 'a') as ud:
        writer_ud = writer(ud)
        writer_ud.writerow(user_data)
        ud.close()
