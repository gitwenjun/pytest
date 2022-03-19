# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/10 18:44
@作者 ： 王齐涛
@文件名称： all_interface.py
'''
import json
import allure
import pytest
from common.all_paths import CASE_PATH,DATA_PATH
from common.all_request import AllRequest
from common.get_url import get_url
from common.read_yaml import ReadYaml
from utils.console_fmt import ConsoleFmt


case_data = ReadYaml().read_yaml(CASE_PATH + "test_all_shopping")


@allure.epic("购物流程")
class TestAllInterface:
    # print(CASE_PATH + "test_all_shopping")

    @pytest.mark.usefixtures('meici')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("args", case_data)
    def test_02(self,args):
        try:
            session = ReadYaml().read_yaml(DATA_PATH + r"\\ecshop_session")  #获取写在yaml文件中的session
            name = args["name"]
            url = get_url("DEV_HTTP","http") + args["request"]["url"]
            method = args["request"]["method"]
            params = args["request"]["params"]
            # print(params)
            # 这里是个笨方法，是对yaml文件中的session运用操作dict的方式重新赋值
            if session:    # 先判断迭代对象是否为空,不然报类型错误：'NoneType’对象不是可迭代的
                params["session"] = (session["session"])
            data = {"json": json.dumps(params)}  # 该接口传参的类型
            print(data)
            exc_message = str(args["assert"][1]["equals"])
            # print(type(exc_message))
            # print(url,data,method)
            re = AllRequest().all_send_request(method=method, url=url, data=data)   # 调用封装的接口方法
            re.encoding = "utf-8"
            act_message = str(re.json()["status"])
            ConsoleFmt().all_console_fmt(name_case=name, url=url, data=data, method=method, response=re.json(),
                                         exc=exc_message, act=act_message)  # 调用断言样式
        except Exception:
            raise




if __name__ == '__main__':
    pytest.main(["-s","all_interface.py"])
