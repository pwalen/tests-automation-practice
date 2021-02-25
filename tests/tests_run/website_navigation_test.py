import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import home_page, category_page_for_woman


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_home_page_content_visible(self):
        self.assertTrue(home_page.content_visible(self.driver))

    def test2_category_page_for_woman_visible(self):
        home_page.click_women_button(self.driver)
        self.assertTrue(category_page_for_woman.woman_on_banner_visible(self.driver))

    def test3_logo_is_clickable(self):
        home_page.click_women_button(self.driver)
        category_page_for_woman.click_logo(self.driver)
        self.assertTrue(home_page.content_visible(self.driver))

    def test4_display_product_on_hover(self):
        self.assertTrue(home_page.content_visible(self.driver))
        home_page.hover_over_faded_short_tshirts(self.driver)
        self.assertTrue(home_page.quick_view_button_displayed(self.driver))
        self.assertTrue(home_page.add_to_cart_button_displayed(self.driver))
        self.assertTrue(home_page.more_button_displayed(self.driver))
        self.assertTrue(home_page.faded_short_tshirts_name_displayed(self.driver))
        self.assertTrue(home_page.faded_short_tshirts_price_displayed(self.driver))

    def test5_popup_title_product_successfully_added_visible(self):
        self.assertTrue(home_page.content_visible(self.driver))
        home_page.hover_over_faded_short_tshirts(self.driver)
        home_page.click_add_to_cart_button(self.driver)
        self.assertTrue(home_page.icon_ok_on_popup_displayed(self.driver))
        self.assertTrue(home_page.popup_tittle_product_successfully_added_displayed(self.driver))


if __name__ == '__main__':
    unittest.main()
