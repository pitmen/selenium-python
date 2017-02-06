import unittest

from selenium import webdriver
from page import GooglePage
from builtins import bool

class Teste(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome('C:/automacao/chromedriver.exe')
        inst.driver.get('http://www.google.com')
        
    def setUp(self):
        print('setup')   
        
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()   
    
    def testName(self):
        page = GooglePage(self.driver)
        page.search()   
        page.press_enter()
        bool = page.is_correct_title()
        self.assertTrue(bool, 'teste')
              
if __name__ == '__main__':
    unittest.main()         