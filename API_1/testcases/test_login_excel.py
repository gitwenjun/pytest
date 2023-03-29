import pytest
from common.all_requests import RequestHandler
from common.excel_operate import ExcelOperate
from common.log_handler import logger
from common.request_excel import ExcelRequestUtil
from common.request_util import RequestUtil
from common.yaml_handler import YamlHandler
from common.assert_response import AssertResponse
import allure

from util.consel_fmt import ConselFmt
from util.template_par import Template_paramse


@allure.epic("会员接口总体描述")
class TestLoginQuery:

    # @allure.feature("会员登录接口")
    # @allure.title("会员登录接口用例")
    @allure.step("第一步")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.issue("https://www.baidu.com",name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com",name="测试用例的链接")
    @pytest.mark.test
    @pytest.mark.L1
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("arg", ExcelOperate("login_test.xls").read_excel())
    def test_reg(self, arg):
        allure.dynamic.feature(arg["feature"])
        allure.dynamic.title(arg["name"])
        ExcelRequestUtil(YamlHandler()).stand_yaml(arg)

    # @allure.feature("修改会员扩展名接口")
    # @allure.title("修改会员信息测试用例")
    @allure.step("第二步")
    @allure.severity(allure.severity_level.MINOR)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.L2
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("arg",ExcelOperate("login_test.xls").read_excel())
    def test_change_info(self,arg):
        location = {"location":"广东12"}
        args = Template_paramse().replase_para(arg,location)
        # logger.debug(f"返回结果为：{args}")
        ConselFmt().get_result_assert(args)

    # @allure.feature("会员查询接口")
    # @allure.title("会员查询接口用例")
    @allure.step("第三步")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.test
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("arg",ExcelOperate("query_test.xls").read_excel())
    def test_query(self, arg):
        allure.dynamic.feature(arg["feature"])
        allure.dynamic.title(arg["name"])
        ExcelRequestUtil(YamlHandler()).stand_yaml(arg)


if __name__ == '__main__':
    pytest.main("-vs","test_login_query.py")