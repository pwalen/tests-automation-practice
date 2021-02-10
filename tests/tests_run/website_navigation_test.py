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


if __name__ == '__main__':
    unittest.main()
