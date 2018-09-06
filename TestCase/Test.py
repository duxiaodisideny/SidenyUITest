import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Config.config import ConfigMethod,DRIVER_PATH

class TestBaidu(unittest.TestCase):

    URL = ConfigMethod().get('URL')

    locator_lw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class,"result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_lw).send_keys('I Love you')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
        print('\n')

    def test_search_1(self):
        self.driver.find_element(*self.locator_lw).send_keys('I Fuck you')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)



if __name__ == '__main__':
    unittest.main()