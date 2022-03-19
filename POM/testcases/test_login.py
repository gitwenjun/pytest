from time import sleep
import allure
import pytest
from selenium import webdriver

from Common.logs import logger
from Common.screenshot import ScreenShot
from Page.login_av import LoginAv
from Common.yaml_av import load_yaml

@allure.epic('AV登录的总体描述')
@allure.feature('登录模块')
class Test_login:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.lg = LoginAv(self.driver)

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    @allure.story('AV登录用例')
    @allure.title('登录成功用例')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://www.baidu.com',name='链接测试用例A')
    @pytest.mark.parametrize('update',load_yaml('G:\Project\Pom\Date\yaml_login.yaml'))
    def test_login_01(self,update):

        try:
            self.lg.login(**update['login'])
            sleep(2)
            # 断言定位到元素
            act = self.lg.ast()
            assert act
            ScreenShot().screen_shot(self.driver, '登录成功_')
        except Exception as e:
            ScreenShot().screen_shot(self.driver,'登录失败_')
            print(e)


if __name__ == '__main__':
    pytest.main(['-s','--alluredir=../Report'])