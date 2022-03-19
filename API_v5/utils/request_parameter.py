# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/9 14:54
@作者 ： 王齐涛
@文件名称： request_parameter.py
'''
import json
from common.all_paths import DATA_PATH
from common.all_request import AllRequest
from common.get_url import get_url
from common.read_yaml import ReadYaml
from utils.console_fmt import ConsoleFmt

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}


class RequestParameter:

    def __get_yaml_parameter(self, args):
        """
        通过读取yaml文件中的用例参数，返回参数供下面的方法调用
        :param args:
        :return:
        """
        name = args["name"]
        url = get_url("DEV_HTTP","http") + args["request"]["url"]
        method = args["request"]["method"]
        params = args["request"]["params"]
        session = ReadYaml().read_yaml(DATA_PATH + r"\\ecshop_session")  # 调用读取yaml文件的方法，获取session
        # headers = args["request"]["headers"]
        if session:    # 先判断迭代对象是否为空,不然报类型错误：'NoneType’对象不是可迭代的
            params["session"] = (session["session"])    # 利用字典的特点替换参数
        data = {"json": json.dumps(params)}  # 该接口传参的类型，只有这样传参才能访问成功
        return name, url, method, data

    def get_request_result(self, parameter):
        """
        获取请求成功后的结果
        :param parameter:
        :return:
        """
        name, url, method, data = self.__get_yaml_parameter(parameter)       # 调用内部方法得到参数
        re = AllRequest().all_send_request(method=method, url=url, data=data)   # 调用封装的接口,如果需要header，可以在这个接口入口直接添加
        re.encoding = "utf-8"
        return re

    def get_request_assert(self, args, re):
        """
        断言操作
        :param args: yaml文件中的用例参数
        :param re: 请求返回的结果
        :return:
        """
        name, url, method, data = self.__get_yaml_parameter(args)
        exc_message = str(args["assert"][1]["equals"])  # 获得用例中的预期数据
        act_message = str(re.json()["status"])      # 获取请求成功后的实际结果
        ConsoleFmt().all_console_fmt(name_case=name, url=url, data=data, method=method,
                                     response=re.json(), exc=exc_message, act=act_message)   # 调用封装的断言样式（方法内部进行了断言）


if __name__ == '__main__':
    aa ={'name': '测试用例1：进入商品ID为134的页面', 'request': {'method': 'post', 'url': '/goods', 'params': {'goods_id': '1500', 'goods': '120', 'session': None}}, 'assert': [{'equals': {'status_code': 200}}, {'equals': {'succeed': 1}}]}


