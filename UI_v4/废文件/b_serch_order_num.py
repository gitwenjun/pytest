# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 15:49
@作者 ： 王齐涛
@文件名称： b_serch_order_num.py 
'''
from selenium.webdriver.common.by import By
from page.Base import Base


class SerchOrderNumPage(Base):
    """
    封装定位元素
    """
    # url = Base.url + "/admin/index.php"
    __input_order_num = (By.ID, "order_sn")
    __serch_control = (By.NAME, "query")



    """
    封装页面操作
    """
    def serch_order_num(self,order_num):
        """
        订单查询（输入订单号）
        :param order_num:
        :return:
        """
        # self.open_url()
        self.send_keys(self.__input_order_num,order_num)
        self.click(self.__serch_control)