# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/10 18:44
@作者 ： 王齐涛
@文件名称： all_interface.py
'''

import allure
import pytest
from common.all_paths import CASE_PATH
from common.read_yaml import ReadYaml
from utils.request_parameter import RequestParameter
from utils.request_replace_parameter import RequestReplaceParameter


@allure.epic("购物流程")
@pytest.mark.usefixtures('meici')
class TestUserLogin:

    @pytest.mark.parametrize("args", ReadYaml().read_yaml(CASE_PATH + "go_goods_page"))
    def test_go_goods_page(self, args):
        """进入商品编号XXX首页"""
        data = {"goods_number": "134"}
        RequestReplaceParameter().get_request_and_assert(args, data)

    # @pytest.mark.skip("跳过")
    @pytest.mark.parametrize("args", ReadYaml().read_yaml(CASE_PATH + "check_harvest_address"))
    def test_check_harvest_address(self, args):
        """查看收获地址"""
        re = RequestParameter().get_request_result(args)
        RequestParameter().get_request_assert(args, re)

    # @pytest.mark.skip("跳过")
    @pytest.mark.parametrize("args", ReadYaml().read_yaml(CASE_PATH + "check_my_collection"))
    def test_check_my_collection(self, args):
        """查看收藏的商品"""
        re = RequestParameter().get_request_result(args)
        RequestParameter().get_request_assert(args, re)

    @pytest.mark.parametrize("args", ReadYaml().read_yaml(CASE_PATH + "test_all_shopping"))
    def test_all_shopping(self, args):
        """添加商品到下单的过程"""
        re = RequestParameter().get_request_result(args)
        RequestParameter().get_request_assert(args, re)

if __name__ == '__main__':
    pytest.main(["-s", "test_user_all.py"])

