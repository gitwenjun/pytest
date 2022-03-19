# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 11:10
@作者:   王齐涛
@文件:   conftest.py 
"""
import pytest
from common.all_paths import DATA_PATH
from common.read_yaml import ReadYaml
from common.logger_handler import GetLogger


# 表示每次再请求时，要清除上次请求获取到的session，不然每请求一次都会记录一次
@pytest.fixture(scope="session", autouse=False)
def clear_session():
    ReadYaml().clear_yaml(DATA_PATH + r"\\ecshop_session")
    yield

#
# @pytest.fixture()
# def meici():
#     log = GetLogger()
#     log.info(" 测试开始")
#     yield
#     log.info(" 测试结束")



