# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/29 10:02
@作者 ： 王齐涛
@文件名称： a_get_order_num.py
'''
from selenium.webdriver.common.by import By

from page.Base import Base


class GetOrderNumPage(Base):
    """
    封装定位元素
    """
    # url = Base.url + "/flow.php?step=done"
    order_num = (By.XPATH, "//font[@style='color:red']")
    succeed_txt = (By.XPATH, "//div[@class='flowBox']//h6")





    """
    封装页面操作
    """
    def get_order_num(self):
        """
        获取订单成功后的订单号
        :return:
        """
        # self.open_url(self.url)
        goods_order_number = self.gain(self.order_num)
        return goods_order_number



    def get_order_succeed_text(self):
        """
        获取订单成功的后的文本内容
        :return:
        """
        order_succeed_text = self.gain(self.succeed_txt)
        return order_succeed_text