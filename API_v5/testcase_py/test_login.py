# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 13:47
@作者:   王齐涛
@文件:   demo2.py 
"""
import allure
import pytest
from common.all_paths import CASE_PATH,DATA_PATH
from common.all_request import AllRequest
from common.get_url import get_url
from common.read_yaml import ReadYaml
from utils.console_fmt import ConsoleFmt


@allure.epic("登录获取session")
class TestLogin:

    @pytest.mark.usefixtures('meici')
    # 定义用例的执行顺序
    @pytest.mark.run(order=0)
    # 调用yaml文件中，通过parametrize装饰器将数据存放在变量args中，然后再调用
    @pytest.mark.parametrize("args",ReadYaml().read_yaml(CASE_PATH + r"\\get_login_session"))
    def test_01(self,args):
        # print(type(args))
        try:
            name = args["name"]
            url = get_url("DEV_HTTP","http") + args["request"]["url"]
            data = args["request"]["params"]
            method = args["request"]["method"]
            exc_message = str(args["assert"][1]["equals"])  # 获取yaml文件中的预期结果
            # print(type(exc_message))
            # print(url,data,method)
            # print(data)
            re = AllRequest().all_send_request(method=method, url=url, data=data)  # 调用统一的请求方式
            # print(re.json())
            act_message = str(re.json()["status"])  # 获取请求成功后的响应结果
            if exc_message in act_message:      # 判断预期结果是不是在响应结果中
                sid = re.json()["data"]["session"]["sid"]
                uid = re.json()["data"]["session"]["uid"]
                # print(re.json()["data"]["session"])
                # 获取请求成功后的session，然后调用方法将值写入到yaml文件中方便调用
                ReadYaml().write_yaml(DATA_PATH + r"\\ecshop_session", {"session": {"uid": f"{uid}", "sid": f"{sid}"}})
                # 调用方法，进行断言（定义了4种方法）
            ConsoleFmt().all_console_fmt(name_case=name, url=url, data=data, method=method, response=re.json(),
                                         exc=exc_message,act=act_message)   # 调用断言样式
        except Exception:
            raise


if __name__ == '__main__':
    pytest.main(["-sv","test_login.py"])