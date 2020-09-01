"""
Google search test suite
"""

import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pages import page
from helper import help

class TestGoogleSearch(unittest.TestCase):
    """Google search test suite"""

    def setUp(self):
        """Start web driver"""
        self.page = page()
        self.driver = webdriver.Chrome()
        self.helper = help(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.google.com/')
        pageTitle = self.driver.title
        assert "Google" in pageTitle
        

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Check for basic google search"""
        try:
            page.search(self, "Tensorflow")   # search for proper search tag
            page.checkresults_are_displayed(self)
            assert "No results found." not in self.driver.page_source
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """Check for irrelevant search tag"""
        try:
            page.search(self, "dcbsudcjcnsdicbdicbdicbweyifcwecdi")   # search for irrelevant search tag
            assert "No results found" in self.driver.page_source
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_3(self):
        """ Check for suggestion on wrong keyword"""
        try:
            page.search(self, "Javacript events")   # search for wrong keyword
            page.getSearchSuggestionText(self, "Javascript events")   # expect for suggestion
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_4(self):
        """ fvbheubrfierfbierfefergtrhb """
        try:
            page.search(self, "Angular.io")  # search for technology term
            page.checkRelevantResult(self, "https://angular.io/")  # expect the technology website url in results
        except NoSuchElementException as ex:
            self.fail(ex.msg)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogleSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)