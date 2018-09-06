import os,time,unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Config.config import ConfigMethod,DRIVER_PATH

class TestBaidu(unittest.TestCase):

    URL = ConfigMethod().get('URl')

    locator_lw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class,"result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def Case1(self):
        self.driver.find_element(*self.locator_lw).send_keys('selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        links = self.find_element(*self.locator_result)
        for link in links:
            print(link.text)

    def Case2(self):
        self.driver.find_element(*self.locator_lw).send_keys('pythonselenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        links = self.find_element(*self.locator_result)
        for link in links:
            print(link.text)



if __name__ == '__main__':
    unittest.main