import unittest
import time
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dalportodev.com/")

    def test_verify_page_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "DALPORTODEV title not found as expected."

    def test_search_test_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        
        #Sets the text of search textbox to "pycon"
        main_page.click_search_button()
        time.sleep(1)
        main_page.search_text_element = "test"
        main_page.enter_search_string()
        time.sleep(1)
        main_page.submit_enter_button()
        time.sleep(4)
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No expected search results found."

    def test_search_garbage_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Sets the text of search textbox to "pycon"
        main_page.click_search_button()
        time.sleep(1)
        main_page.search_text_element = "garbage"
        main_page.enter_search_string()
        time.sleep(1)
        main_page.submit_enter_button()
        time.sleep(4)
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found() is False, "Garbage negative test returned unexpected result."

    def tearDown(self):
        time.sleep(4)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()