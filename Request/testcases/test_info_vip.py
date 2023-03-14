# -*-coding:GBK -*-
import allure
import pytest
from time import sleep
from Common.logs import logger
from Common.replace_params import Relace
from Common.yaml_req import YamlParams
from testcases.test_login import TestLogin
from util.request_result import ResuiltParams


@allure.epic("会员接口总体描述")
@allure.feature('会员接口测试用例')
class TestInfoVip:
    def setup_class(self):
        logger.info("执行登录，获取session")
        TestLogin().test_login_01
        sleep(2)

    def teardown_class(self):
        YamlParams().yaml_clean("G:\Project\Request\Data\session.yaml")
        logger.info("用例执行完成，清除session")

    @allure.story('获取会员信息接口')
    @allure.description('获取用例描述')
    @allure.title('获取会员用例title==》')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('http://www.baidu.com',name="点击跳转测试用例=>")
    @allure.step('步骤一')
    @pytest.mark.L1
    @pytest.mark.run(order=2)
    # @pytest.mark.skip(reason="测试跳过")
    @pytest.mark.parametrize('arg',YamlParams().yaml_read("G:\Project\Request\Data\info_vip.yaml"))
    def test_info_01(self, arg):
        ResuiltParams().resuilt_ast_mgs(arg)

    @allure.story('修改会员信息接口')
    @allure.description('修改用例描述')
    @allure.title('修改会员用例title==》')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('http://www.baidu.com', name="点击跳转测试用例=>")
    @allure.step('步骤一')
    @pytest.mark.L1
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('arg', YamlParams().yaml_read("G:\Project\Request\Data\change_info.yaml"))
    def test_change_local(self,arg):
        ext_info = {"location": "成都2"}
        arg = Relace().replace_dict(arg,ext_info) # 替换yaml文件中的$参数
        ResuiltParams().resuilt_ast_ststus(arg)


if __name__ == '__main__':
    pytest.main(['-v'])
    # pytest.main(['-v','q','--reruns','1','--reruns-delay','2','-n','auto'])
