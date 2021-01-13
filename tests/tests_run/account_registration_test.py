import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import home_page, authentication_page, account_creation_page, successful_registration_page
from tests.helpers.user_data_collection import *


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_home_page_content_visible(self):
        self.assertTrue(home_page.home_page_content_visible(self.driver))

    def test2_authentication_page_visible(self):
        home_page.go_to_authentication_page(self.driver)
        self.assertTrue(authentication_page.my_account_header_visible(self.driver))

    def test3_email_acceptance(self):
        home_page.go_to_authentication_page(self.driver)
        authentication_page.correct_email_submission(self.driver)
        authentication_page.click_create_account_button(self.driver)
        self.assertTrue(account_creation_page.account_creation_form_visible(self.driver))

    def test4_user_registration(self):
        home_page.go_to_authentication_page(self.driver)
        authentication_page.correct_email_submission(self.driver)
        authentication_page.click_create_account_button(self.driver)
        account_creation_page.account_creation_form_visible(self.driver)
        account_creation_page.radio_button_mr_selection(self.driver)
        account_creation_page.correct_firstname1_submission(self.driver)
        account_creation_page.correct_lastname1_submission(self.driver)
        account_creation_page.correct_password_submission(self.driver)
        account_creation_page.correct_birth_year_selection(self.driver)
        account_creation_page.correct_birth_month_selection(self.driver)
        account_creation_page.correct_birth_day_selection(self.driver)
        account_creation_page.checkbox_newsletter_selection(self.driver)
        account_creation_page.checkbox_special_offers_selection(self.driver)
        account_creation_page.correct_address1_submission(self.driver)
        account_creation_page.correct_city_submission(self.driver)
        account_creation_page.correct_state_selection(self.driver)
        account_creation_page.correct_postcode_submission(self.driver)
        account_creation_page.correct_phone_mobile_submission(self.driver)
        account_creation_page.correct_alias_submission(self.driver)
        account_creation_page.register_button_click(self.driver)
        self.assertTrue(successful_registration_page.welcome_message_displayed(self.driver))
        export_user_data_to_csv()

    def test5_user_registration_and_logout(self):
        home_page.go_to_authentication_page(self.driver)
        authentication_page.correct_email_submission(self.driver)
        authentication_page.click_create_account_button(self.driver)
        account_creation_page.account_creation_form_visible(self.driver)
        account_creation_page.radio_button_mr_selection(self.driver)
        account_creation_page.correct_firstname1_submission(self.driver)
        account_creation_page.correct_lastname1_submission(self.driver)
        account_creation_page.correct_password_submission(self.driver)
        account_creation_page.correct_birth_year_selection(self.driver)
        account_creation_page.correct_birth_month_selection(self.driver)
        account_creation_page.correct_birth_day_selection(self.driver)
        account_creation_page.checkbox_newsletter_selection(self.driver)
        account_creation_page.checkbox_special_offers_selection(self.driver)
        account_creation_page.correct_address1_submission(self.driver)
        account_creation_page.correct_city_submission(self.driver)
        account_creation_page.correct_state_selection(self.driver)
        account_creation_page.correct_postcode_submission(self.driver)
        account_creation_page.correct_phone_mobile_submission(self.driver)
        account_creation_page.correct_alias_submission(self.driver)
        account_creation_page.register_button_click(self.driver)
        successful_registration_page.logout_button_click(self.driver)
        self.assertTrue(authentication_page.my_account_header_visible(self.driver))
        export_user_data_to_csv()


if __name__ == '__main__':
    unittest.main()
