from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    #locator = (By.ID, 'q')
    locator = (By.ID, 'headerSearch')


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    #search_text_element = SearchTextElement()
    search_text_element = ''

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "DALPORTODEV" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def enter_search_string(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_TEXT_BOX)
        element.send_keys(self.search_text_element)

    def click_search_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def submit_enter_button(self):
        """Sends enter key"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_TEXT_BOX)
        element.send_keys(Keys.ENTER)

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "Your search did not match any documents." not in self.driver.page_source