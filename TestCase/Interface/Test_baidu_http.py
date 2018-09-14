import unittest
from ConfigMethod.config import ConfigMethod
from Utils.Client import HTTPclient
from Utils.Log import logger
from Utils.HTMLTestRunner import HTMLTestRunner

class TestbaiduHTTP(unittest.TestCase):
    URL = ConfigMethod().get('URL')

    def setUp(self):
        self.client = HTTPclient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道',res.text)

testunit1 = unittest.TestSuite()
testunit1.addTest(TestbaiduHTTP("test_baidu_http"))
report = '/Users/duxiaodi/PycharmProjects/SidenyUITest/Report/report.html'
fp1 = open('/Users/duxiaodi/PycharmProjects/SidenyUITest/Report/report.html', 'wb')
runner = HTMLTestRunner(stream=fp1, title='测试报告', description='测试执行情况')
runner.run(testunit1)
fp1.close()