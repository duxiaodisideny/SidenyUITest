import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ConfigMethod.config import ConfigMethod,DRIVER_PATH,DATA_PATH,REPORT_PATH
from Utils.Log import logger
from Utils.File_reader import ExcelReader
from Utils.HTMLTestRunner import HTMLTestRunner
import os
from Utils.Mail import Email

class TestBaidu(unittest.TestCase):

    URL = ConfigMethod().get('URL')
    excel = DATA_PATH + '/dxd.xlsx'

    locator_lw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class,"result")]/h3/a')

    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
    #     self.driver.get(self.URL)
    #
    # def tearDown(self):
    #     self.driver.quit()


    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    # def test_search_0(self):
    #     self.driver.find_element(*self.locator_lw).send_keys('I Love you')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(3)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)
    #
    # def test_search_1(self):
    #     self.driver.find_element(*self.locator_lw).send_keys('I Fuck you')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(3)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    # def test_search_2(self):
    #     datas = ExcelReader(self.excel).data
    #     for d in datas:
    #         with self.subTest(data=d):
    #             self.sub_setUp()
    #             self.driver.find_element(*self.locator_lw).send_keys(d['luyumeng'])
    #             self.driver.find_element(*self.locator_su).click()
    #             time.sleep(2)
    #             links = self.driver.find_elements(*self.locator_result)
    #             for link in links:
    #                 logger.info(link.text)
    #             self.sub_tearDown()

    def test_search_3(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_lw).send_keys(d['Tname'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


# if __name__ == '__main__':
#     # unittest.main(verbosity=2)
#     report = './report.html'
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(stream=f, verbosity=1, title='测试报告', description='测试执行情况')
#         runner.run(TestBaidu('test_search_3'))


testunit = unittest.TestSuite()
testunit.addTest(TestBaidu("test_search_3"))
report = '/Users/duxiaodi/PycharmProjects/SidenyUITest/Report/report.html'
fp = open('/Users/duxiaodi/PycharmProjects/SidenyUITest/Report/report.html', 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(testunit)
fp.close()
e = Email(title='百度搜索测试报告',
          message='This is report',
          receiver='duyang.li@119xiehui.com',
          server='smtp.exmail.qq.com',
          sender='xiaodi.du@119xiehui.com',
          password='sg2NpQHir3DPvaKj',
          path=report)
e.send()
