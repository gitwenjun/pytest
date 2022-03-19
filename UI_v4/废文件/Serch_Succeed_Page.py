# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/28 19:52
@作者 ： 王齐涛
@文件名称： Serch_Succeed_Page.py 
'''
from selenium.webdriver.common.by import By
from 废文件.a_front_end_login import *

class serch_succeed(Base):
    """
    封装定位元素
    """

    add_shopping_cart_contorl = (By.XPATH, "//img[@src='themes/default/images/bnt_cat.gif']")  # 加入购物车
    collect_goods_control = (By.LINK_TEXT ,"收藏")


    """
    封装页面操作
    """
    def Buy_Goods(self):
        """
        加入购物车 按钮
        :return:
        """
        self.click(self.add_shopping_cart_contorl)


    def Collect(self):
        """
        加入收藏 按钮
        :return:
        """
        try:
            self.click(self.collect_goods_control)
        except:
            pass

