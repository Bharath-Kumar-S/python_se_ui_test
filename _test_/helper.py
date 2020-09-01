
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class help():

    def __init__(self, driver):
        self.driver=driver

   
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).click()
    
    
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    
    def enter_text_and_hit_entet(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        el = self.driver.find_element(*by_locator)
        el.send_keys(text)
        el.send_keys(Keys.RETURN)

    
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))

    
    def is_visible(self,by_locator):
        el = self.driver.find_element(*by_locator)
        return el.is_displayed()
