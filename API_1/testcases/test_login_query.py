import pytest
from common.all_requests import RequestHandler
from common.log_handler import logger
from common.yaml_handler import YamlHandler
from common.assert_response import AssertResponse
import allure

from util.consel_fmt import ConselFmt
from util.template_par import Template_paramse


@allure.epic("会员登录查询接口总体描述")
class TestLoginQuery:

    @allure.feature("会员登录接口")
    @allure.title("会员登录成功测试用例")
    @allure.step("第一步")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.issue("https://www.baidu.com",name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com",name="测试用例的链接")
    @pytest.mark.smoke
    @pytest.mark.L1
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("arg",YamlHandler().read_yaml("./data/login.yaml"))
    def test_reg(self,arg):
        name = arg["name"]
        method = arg["request"]["method"]
        url = arg["request"]["url"]
        paramse = arg["request"]["paramse"]
        res_exp = arg["validata"][1]["contains"]["err_code"]
        response = RequestHandler().sent_request(url=url,method=method,params=paramse).json()
        res_act = response["data"]["err_code"]
        if res_exp == res_act:
            token = response["data"]["token"]
            uuid = response["data"]["uuid"]
            YamlHandler().write_yaml("./data/session.yaml",{"token": token})
            YamlHandler().write_yaml("./data/session.yaml", {"uuid": uuid})
        AssertResponse().assert_equals(name=name,method=method,url=url,parmase=paramse,response=response,response_exp=res_exp,response_act=res_act)

    @allure.feature("修改会员扩展名接口")
    @allure.title("修改会员信息测试用例")
    @allure.step("第二步")
    @allure.severity(allure.severity_level.MINOR)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.L2
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("arg",YamlHandler().read_yaml("./data/change_info.yaml"))
    def test_change_info(self,arg):
        location = {"location":"广东12"}
        args = Template_paramse().replase_para(arg,location)
        # logger.debug(f"返回结果为：{args}")
        ConselFmt().get_result_assert(args)

    @allure.feature("会员查询接口")
    @allure.title("会员查询成功测试用例")
    @allure.step("第三步")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.L3
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("arg", YamlHandler().read_yaml("./data/query.yaml"))
    def test_query(self, arg):
        ConselFmt().get_result_assert(arg)


if __name__ == '__main__':
    pytest.main("-vs","test_login_query.py")