from selenium import webdriver
import unittest
from Utils.HTMLTestRunner import HTMLTestRunner


class Baidu(unittest.TestCase):
    "百度搜索测试"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def test_baidu_search(self):
        "搜索关键字"
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("Selenium3")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()


testunit = unittest.TestSuite()
testunit.addTest(Baidu("test_baidu_search"))
fp = open('./result.html', 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(testunit)
fp.close()

