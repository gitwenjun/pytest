# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/30 16:02
@作者 ： 王齐涛
@文件名称： test_login.py
'''

import allure
import pytest
from page.Base import Base
from common.all_paths import CASE_PATH
from data.global_variable import *
from data.user_data import *
from 废文件.a_check_out import CheckOutPage
from 废文件.a_get_order_num import GetOrderNumPage
from 废文件.a_order_message import OrderMessagePage
from 废文件.a_serch_common_goods import SerchCommonGoodsPage
from 废文件.a_user_centre import UserCentrePage
from 废文件.b_after_end_login import AfterEndLogin
from 废文件.b_complete_order_flow import CompleteOrderFlowPage
from 废文件.b_get_order_state import GetOrderStatePage
from 废文件.b_serch_order_num import SerchOrderNumPage
from common.result_assert import Assert


class TestCustomer:

    @allure.title("正向的测试流程")
    @allure.feature("整个操作流程")
    def test01_login(self,init):
        """Ecshop购物的正向购物流程（详细步骤见 订单流程.text）"""
        SerchCommonGoodsPage(init).serch_common_goods(serch_goods_name)
        CheckOutPage(init).colsing_centre()
        OrderMessagePage(init).order_message(peisong="上门取货",payment="银联电子支付")
        order_number = GetOrderNumPage(init).get_order_num()
        order_succeed_text = GetOrderNumPage(init).get_order_succeed_text()

        Base(init).screenshot("前端订单界面_提交成功截图")

        Assert().assert_message("成功",order_succeed_text)     # 断言订单

        Base(init).new_window(after_url)
        Base(init).switch_new_window()

        AfterEndLogin(init).after_end_login(after_un,after_pw)

        Base(init).switch_frame(order_manage,"订单查询")

        SerchOrderNumPage(init).serch_order_num(order_number)
        CompleteOrderFlowPage(init).complete_order_flow()

        Base(init).switch_old_window()   # 切换到前端
        SerchCommonGoodsPage(init).my_account()
        UserCentrePage(init).operate_order(order_number)

        Base(init).switch_new_window()
        Base(init).switch_frame(order_manage, "订单列表")
        text = GetOrderStatePage(init).get_shipments_state(order_number)

        Base(init).screenshot("后端订单界面_收获确认截图")
        Assert().assert_message("收货确认", text)
        path = CASE_PATH + r"\订单流程.text"
        file_png = open(path, mode='rb').read()
        allure.attach(body=file_png,name="整个正向的测试流程",attachment_type=allure.attachment_type.TEXT)




if __name__ == '__main__':
    pytest.main(["-s","normal_direction_flow.py"])