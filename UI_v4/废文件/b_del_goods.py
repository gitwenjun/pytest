# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/26 22:43
@作者 ： 王齐涛
@文件名称： b_del_goods.py 
'''
from selenium.webdriver.common.by import By

from page.Base import Base


class DelGoodsPage(Base):

    def alone_del_goods(self,goods_name):
        """
        删除单个商品
        :param goods_name:  商品名称
        :return:
        """
        self.click((By.XPATH, f"//span[text()='{goods_name}']//..//..//a[@title='回收站']"))
        self.pop_up_windows()

    # def batch_del_goods(self,goods_name):
    #     self.click(((By.XPATH, f"//span[text()='{goods_name}']//..//..//input")))