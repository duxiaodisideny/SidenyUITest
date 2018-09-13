# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# import unittest
# from ConfigMethod.config import ConfigMethod,DATA_PATH,DRIVER_PATH
# from Utils.File_reader import ExcelReader
# from Utils.Log import logger
#
# class Test(unittest.TestCase):
#
#
#     URL = ConfigMethod().get('URL')
#     excel = DATA_PATH + '/dxd.xlsx'
#
#     def sub_setUp(self):
#         self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
#         self.driver.get(self.URL)
#
#     def sub_tearDown(self):
#         self.driver.quit()
#
#     def test_search_1(self):
#         datas = ExcelReader(self.excel).data
#         action = ActionChains(self.driver)
#         self.driver.find_element_by_xpath('//*[@id="txtlname"]').send_keys(datas['Tname'])
#         self.driver.find_element_by_xpath('//*[@id="txtlpwd"]').send_keys(datas['Tpassword'])
#         time.sleep(3)
#         self.driver.find_element_by_xpath('/html/body/div[3]/form/div/div[3]/input').click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath('/html/body/div[4]/ul/li[2]').click()
#         time.sleep(1)
#         action.move_to_element(self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]/ul/li[1]/div/p'))
#         time.sleep(1)
#         self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]/ul/li[1]/div/ul/li[2]/p').click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="form1"]/div/div[1]/div[1]/div/input[4]').send_keys('TestAuto')
#         self.driver.find_element_by_xpath('//*[@id="beginTime"]').send_keys('2018-09-12 12:10')
#         self.driver.find_element_by_xpath('')
#         self.driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/textarea').send_keys('TestAuto自动化测试自动填写内容')
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#
