# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/11 15:32
@作者 ： 王齐涛
@文件名称： detection_session.py 
'''
from common.all_paths import CASE_PATH
from common.logger_handler import GetLogger
from common.read_yaml import ReadYaml
from testcase_py.test_login import TestLogin

assert_error = "{'succeed': 0, 'error_code': 100, 'error_desc': '您的帐号已过期'}"     # 进行断言的参数
log = GetLogger()


def detection_session(act_message):
    """
    检测session是否不正确或者时效了，如果是的话就重新触发登录，获取新的session
    :param act_message:
    :return:
    """
    if assert_error == act_message:
        login_data = ReadYaml().read_yaml(CASE_PATH + r"\\get_login_session")   # 调用登录函数的参数
        log.error("可能是session时效或者不正确，需要重新登录获取新的session，以下代码表示重新登录！")
        TestLogin().test_01(login_data[0])        # 调用登录函数，返回的是列表，所以是login_data[0]