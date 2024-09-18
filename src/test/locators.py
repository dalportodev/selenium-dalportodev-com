from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BUTTON = (By.CLASS_NAME, 'header-search')
    SEARCH_TEXT_BOX = (By.CLASS_NAME, 'header-search-form-input')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass