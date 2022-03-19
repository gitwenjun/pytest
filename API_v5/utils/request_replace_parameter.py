# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/9 14:54
@作者 ： 王齐涛
@文件名称： request_parameter.py
'''
from common.all_paths import DATA_PATH
from common.all_request import AllRequest
from common.get_url import get_url
from common.read_yaml import ReadYaml
from utils.console_fmt import ConsoleFmt
import json
from utils.convert_data import ConvertData
from utils.detection_session import detection_session

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}


class RequestReplaceParameter:

    @staticmethod
    def __get_yaml_parameter(args, parameter):
        """
        通过读取yaml文件中的用例参数，并进行部分参数替换，返回新的参数供下面的方法调用
        :param args: yaml文件中的用例参数
        :param parameter: 需要替换的参数，传参格式比如：data = {"goods_number": "134"}
        :return:
        """
        try:
            amend_args = ConvertData.convert_data_text(args, parameter)  # 调用封装的参数替换方法
            name = amend_args["name"]
            url = get_url("DEV_HTTP","http") + amend_args["request"]["url"]  # 调用的封装的获取url方法，拼接
            method = amend_args["request"]["method"]
            params = amend_args["request"]["params"]
            session = ReadYaml().read_yaml(DATA_PATH + r"\\ecshop_session")  # 调用读取yaml文件的方法，获取session
            # headers = args["request"]["headers"]
            if session:    # 先判断迭代对象是否为空,不然报类型错误：'NoneType’对象不是可迭代的
                params["session"] = (session["session"])    # 利用字典的特点替换参数
            data = {"json": json.dumps(params)}  # 接口传参的类型，只有这样传参才能访问成功
            return name, url, method, data
        except Exception:
            raise

    @staticmethod
    def get_request_and_assert(args, replace_parameter):
        """
        获取请求成功后的结果和对结果进行断言
        :param args:
        :param replace_parameter: 要替换的参数
        :return:
        """
        try:
            name, url, method, data = RequestReplaceParameter().__get_yaml_parameter(args, replace_parameter)   # 调用内部方法
            re = AllRequest().all_send_request(method=method, url=url, data=data)    # 调用封装的接口,如果需要header，可以在这个接口入口直接添加
            re.encoding = "utf-8"
            exc_message = str(args["assert"][1]["equals"])  # 获得用例中的预期数据
            act_message = str(re.json()["status"])      # 获取请求成功后的实际结果
            ConsoleFmt().all_console_fmt(name_case=name, url=url, data=data, method=method,
                                         response=re.json(), exc=exc_message, act=act_message)   # 调用封装的断言样式（方法内部进行了断言）
            detection_session(act_message)  # 调用封装的方法判断session是否有效
        except Exception:
            raise


if __name__ == '__main__':
    aa ={'name': '测试用例1：进入商品ID为134的页面', 'request': {'method': 'post', 'url': '/goods', 'params': {'goods_id': '${goods_number}', 'goods': '$haha', 'session': None}}, 'assert': [{'equals': {'status_code': 200}}, {'equals': {'succeed': 1}}]}
    bb = {"goods_number": "150","haha":"120"}


