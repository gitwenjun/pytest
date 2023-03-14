from time import sleep
import allure
import pytest
from selenium import webdriver

from Common.logs import logger
from Common.screenshot import ScreenShot
from Page.login_av import login_page
from Common.yaml_av import read_yaml
@allure.epic('AVUI测试')
@allure.feature('AV登录功能')
class aTestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.lg = login_page(self.driver)
        self.driver.find_element()
    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    @allure.title('登录用例一')
    @allure.story('登录测试用例')
    @allure.link('www.baidu.com',name='测试用例')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('arg',read_yaml('G:\Project\Pom\Date\yaml_login.yaml'))
    def atest_login(self,arg):
        self.lg.login(**arg['login'])
        ScreenShot().screeshotPhoto(self.driver, '登录_')
        assert self.lg.ast()


#
# if __name__ == '__main__':
#     pytest.main(['-vs'])