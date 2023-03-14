import pytest
from common.all_requests import RequestHandler
from common.yaml_handler import YamlHandler
from common.assert_response import AssertResponse
import allure

class TestRegister:
    @allure.epic("会员注册总体描述")
    @allure.feature("会员注册接口")
    @allure.title("会员注册成功测试用例")
    @allure.step("就一步")
    @allure.severity(allure.severity_level.MINOR)
    @allure.issue("https://www.baidu.com", name="禅道BUG的链接")
    @allure.testcase("https://www.jd.com", name="测试用例的链接")
    @pytest.mark.L0
    @pytest.mark.parametrize("arg",YamlHandler().read_yaml("./data/register.yaml"))
    def test_reg(self,arg):
        name = arg["name"]
        method = arg["request"]["method"]
        url = arg["request"]["url"]
        paramse = arg["request"]["paramse"]
        res_exp = arg["validata"][1]["contains"]["err_code"]
        response = RequestHandler().sent_request(method=method,url=url,params=paramse).json()
        res_act = response["data"]["err_code"]
        AssertResponse().assert_equals(name=name,method=method,url=url,parmase=paramse,response_exp=res_exp,response_act=res_act)
        print(response)



if __name__ == '__main__':
    pytest.main("-vs")