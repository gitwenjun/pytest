import pytest
from selenium import webdriver
from common.log_handler import logger
from common.screenshot import Screenshot
from common.yaml_handler import YamlHandler
from page.login import LoginPage
from common.assert_result import AssertResults
import allure

@allure.epic("登录测试接口")
class TestLogin:

    def setup_class(self):
        logger.info(f"---------测试用例开始执行----------")
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        logger.info(f"---------测试用例执行结束----------")
        self.driver.quit()

    @allure.feature("登录用例")
    @allure.title("登录成功测试用例")
    @allure.testcase("www.baidu.com",name="测试用例链接")
    @allure.issue("www.jd.com",name="缺陷链接地址")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize('arg', YamlHandler().read_yaml('./data/login.yaml'))
    def test_login(self, arg):
        with allure.step("第一步输入账号密码"):
            LoginPage(self.driver).login(**arg)
        # html = self.driver.page_source.encode("utf-8")
        # 获取实际结果
        res_text = LoginPage(self.driver).result().text
        # logger.debug(f"测试的值为{res_text}")
        with allure.step("第二步对比实际结果"):
            AssertResults().assert_messges("个人中心",res_text)
        # 截图
        Screenshot.photo_screenshoot(self.driver, "登录")


if __name__ == '__main__':
    pytest.main(['-vs'])
