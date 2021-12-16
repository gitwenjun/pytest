from selenium import webdriver
from PageObject import bing_page
import pytest
from Commom.ym_pars import yaml_params
from Commom.csv_bings import csv_bing_wds
import allure

url = yaml_params('G:\Project\BingSearch\Config\ym_url.yaml','websits','url')
wk = csv_bing_wds('G:\Project\BingSearch\Data\csv_bing.csv')
wk2 = csv_bing_wds('G:\Project\BingSearch\Data\csv_bing2.csv')

@allure.epic('epic,相当于总体描述')
@allure.feature('搜索模块')
class TestBing():
    def setup(self):
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities={'browserName':'chrome'})
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    def teardown(self):
        self.driver.quit()


    @allure.issue("https://www.cnblogs.com/poloyy/p/12219145.html", 'Bug 链接,点我一下')
    @allure.story('中文搜索')
    @allure.title('用例一')
    @allure.severity('critical')
    @allure.step('步骤一')
    @pytest.mark.parametrize('msg', wk)
    def test_serach_01(self,msg):
        bing_page.BingBus(self.driver).bing_b(msg)
        assert '没有找到您要的结果' not in self.driver.page_source

    @allure.testcase("https://www.cnblogs.com/poloyy/", '测试用例,点我一下')
    @allure.story('数字搜索')
    @allure.title('用例二')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('步骤一')
    @pytest.mark.parametrize('msg', wk2)
    def test_serach_02(self,msg):
        bing_page.BingBus(self.driver).bing_b(msg)
        assert '没有找到您要的结果' not in self.driver.page_source

if __name__ == '__main__':
    pytest.main(['-q','-s','--alluredir=./report'])
