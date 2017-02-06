from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GooglePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def search(self):
        self.driver.find_element_by_name('q').send_keys('teste')   
    
    def press_enter(self):
        self.driver.find_element_by_name('q').send_keys(Keys.ENTER)
        
    def is_correct_title(self): 
        return self.driver.title == 'Google'       