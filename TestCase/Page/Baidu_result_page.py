from selenium.webdriver.common.by import By
from TestCase.Page.Baidu_main_page import BaiduMainPage

class BaiDuResultPage(BaiduMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)