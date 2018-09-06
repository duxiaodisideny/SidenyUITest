# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# URL = "https://www.baidu.com"
#
# locator_lw = (By.ID,'kw')
# locator_su = (By.ID,'su')
# locator_result = (By.XPATH,'//div[contains(@class,"result")]/h3/a')
#
# driver = webdriver.Chrome()
# driver.get(URL)
# driver.find_element(*locator_lw).send_keys('selenium 测试')
# driver.find_element(*locator_su).click()
# time.sleep(2)
# links = driver.find_elements(*locator_result)
# for link in links:
#     print(link.text)
# driver.quit()