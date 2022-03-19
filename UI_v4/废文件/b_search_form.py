# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/29 14:16
@作者 ： 王齐涛
@文件名称： b_search_form.py
'''
from selenium.webdriver.common.by import By
from page.Base import Base


class SerchFromPage(Base):
    """
    封装定位元素
    """
    __search_order_number = (By.NAME, "order_sn")
    __search_order_name = (By.NAME, "consignee")
    __order_state = (By.NAME,"status")
    __search_control = (By.XPATH, "//input[@value=' 搜索 ']")



    """
    封装页面操作
    """
    def serch_order(self,orderID=None,orderName=None,orderState="请选择..."):
        """
        在订单列表中，根据订单的类型来搜索订单
        :param orderID: 订单号（无默认值）
        :param orderName: 订单人名字（无默认值）
        :param orderState: 订单状态（ 默认 请选择....）

        """
        if orderID != None:
            self.send_keys(self.__search_order_number,orderID)
        elif orderName != None:
            self.send_keys(self.__search_order_name,orderName)
        elif orderName != None and orderID != None:
            self.send_keys(self.__search_order_number, orderID)
            self.send_keys(self.__search_order_name, orderName)

        self.select(self.__order_state,"text",orderState)
        self.click(self.__search_control)

        self.click((By.LINK_TEXT,f"{orderID}"))   #通过点击订单编号进行订单详情