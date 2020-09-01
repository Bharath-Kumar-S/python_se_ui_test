
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locators import Locator
from helper import help



class page:
   
    def __init__(self):
        Locator()

    def search(self, text):
        help.enter_text_and_hit_entet(self,Locator.SEARCH_TEXTBOX, text)

    def getSearchSuggestionText(self, text):
        return help.assert_element_text(self, Locator.SEARCH_SUGGESTION, text)
    
    def checkRelevantResult(self, url):
        result = (By.CSS_SELECTOR, "a[href=\"" + url + "\"]")
        resultlink = help.is_visible(self, result)
        assert resultlink == True

    def checkresults_are_displayed(self):
        results = help.is_visible(self, Locator.SEARCH_RESULTS)
        assert results == True