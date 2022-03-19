# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/26 17:49
@作者 ： 王齐涛
@文件名称： add_goods.py 
'''
import allure
import pytest

from page.Base import Base
from data.global_variable import *
from 废文件.b_add_goods import AddGoodsPage
from 废文件.b_del_goods import DelGoodsPage
from common.result_assert import Assert


class TestAddGoods:


    # @allure.description("这里填写的内容就是报告中的描述，另外一种方法就是在函数方法下面写")
    @allure.epic("epic相当于总体描述，比如用在class上面")
    @allure.feature("后端操作")     # 类似于一级目录，如果feature中参数一样，就表示只有一个一级目录，下面有两个二级目录
    @allure.title("添加商品-输入正确的必填参数") # 用例的标题
    @allure.story("后端添加商品操作")  # 类似于二级目录
    def test_add_goods(self, after_init):
        """后端添加商品"""
        with allure.step("step1:切换框架，点击添加新商品"):     # 用例的步骤，另一种方法是@allure.step
            Base(after_init).switch_frame(goods_manage, "添加新商品")
        return_value= AddGoodsPage(after_init).add_goods()
        # goods_name = return_value[0]
        succeed_text = return_value[1]
        with allure.step("step2:输入必填项，点击确认"):
            Base(after_init).screenshot("添加商品页面_商品信息详情")
        Assert().assert_message("添加商品成功", succeed_text)


    # @pytest.mark.dependency(depends=["test_add_goods"])  # 控制用例的依赖关系,如果test_add_goods用例失败，就跳过该用例
    @allure.title("删除商品-删除添加成功后的商品")
    @allure.feature("后端操作")
    @allure.story("后端删除商品操作")
    def test_del_goods(self, after_init):
        """后端删除商品"""
        with allure.step("step1:刷新浏览器界面"):
            Base(after_init).browser_refresh()
        with allure.step("step2:切换框架，点击商品列表"):
            Base(after_init).switch_frame(goods_manage, "商品列表")
        with allure.step("step3:删除商品-{input_new_goods_name}"):
            DelGoodsPage(after_init).alone_del_goods(input_new_goods_name)


if __name__ == '__main__':
    pytest.main(["-s","add_goods.py"])