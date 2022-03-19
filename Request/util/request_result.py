import json
from Common.request import Request
from Common.yaml_req import YamlParams
from Common.logs import logger
import jsonpath
from util.consel_fmt import ConselFmt


class ResuiltParams:

    #获取token/uuid
    def __get_params(self, arg):
        try:
            name = arg['name']
            method = arg['request']['method']
            url = arg['request']['url']
            data = arg['request']['data']
            session = YamlParams().yaml_read("G:\Project\Request\Data\session.yaml")
            if session:
                data["token"] = session['session']["token"]
                data['uuid'] = session['session']['uuid']
            return name,method,url,data
        except Exception as e:
            raise e

    # 获取结果，断言响应码
    def resuilt_ast_ststus(self,arg):
        name,method,url,data = self.__get_params(arg)
        exc = arg['assert'][0]['eq']['err_code']  # 预期信息
        res = Request().request_hanle(method=method, url=url, json=data).json()
        act = res['data']['err_code']  # 实际信息
        # logger.error(f"类型为：{type(act)}")
        ConselFmt().status_consel_fmt(name=name, method=method, url=url, data=data, response=res, exc=exc, act=act)

    # 获取结果，断言响应信息
    def resuilt_ast_mgs(self, arg):
        name, method, url, data = self.__get_params(arg)
        exc = arg['assert'][1]['contains']['rolename']  # 预期信息
        res = Request().request_hanle(method=method, url=url, json=data).json()
        act = jsonpath.jsonpath(res,'$.data..rolename')  # 实际信息
        logger.error(f"类型未：{type(act)}")
        ConselFmt().message_consel_fmt(name=name, method=method, url=url, data=data, response=res, exc=exc, act=act) # 调用断言

