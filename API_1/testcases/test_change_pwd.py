import allure
import pytest

from common.yaml_handler import YamlHandler
from util.consel_fmt import ConselFmt


class TestChangePwd:

    @allure.feature("修改会员密码接口")
    @allure.title("会员密码修改成功测试用例")
    @allure.step("第N步")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.L4
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("arg", YamlHandler().read_yaml("./data/change_pwd.yaml"))
    def test_change_pwd(self, arg):
        ConselFmt().get_result_assert(arg)
