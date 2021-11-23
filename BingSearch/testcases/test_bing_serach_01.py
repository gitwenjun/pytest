from selenium import webdriver
from PageObject import bing_page
import pytest
from Commom.ym_pars import yaml_params
from Commom.csv_bings import csv_bing_wds

url = yaml_params('G:\Project\BingSearch\Config\ym_url.yaml','websits','url')
wk = csv_bing_wds('G:\Project\BingSearch\Data\csv_bing.csv')
@pytest.mark.parametrize('msg',wk)
class TestBing():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    def teardown(self):
        self.driver.quit()

    def test_serach_01(self,msg):
        bing_page.BingBus(self.driver).bing_b(msg)
        assert '没有找到您要的结果' not in self.driver.page_source

if __name__ == '__main__':
    pytest.main(['-q','-s','--alluredir=./report'])
