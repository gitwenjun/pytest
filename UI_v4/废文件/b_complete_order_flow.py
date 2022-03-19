# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 16:55
@作者 ： 王齐涛
@文件名称： b_complete_order_flow.py 
'''
from selenium.webdriver.common.by import By

from page.Base import Base



class CompleteOrderFlowPage(Base):
    """
    封装定位元素
    """
    __check_order = (By.XPATH, "//a[@id='order_0']")  # 查看订单编号按钮查看信息页面
    __pay_control = (By.XPATH, "//input[@value='付款']")   # 付款按钮
    __operation_note = (By.NAME,"action_note")  # 付款后添加操作备注
    __submit_control = (By.XPATH,"//input[@value=' 确定 ']")   # 确定按钮
    __distribution = (By.XPATH, "//input[@value='配货']")  # 订单界面 配货按钮
    __create_fahuo = (By.XPATH, "//input[@value='生成发货单']")  # 订单界面 生成发货单按钮
    __confirm = (By.XPATH, "//input[@value='确认生成发货单']")  # 订单界面 确认生成发货单按钮
    __go_fahuo = (By.XPATH, "//input[@value='去发货']")  # 订单界面 去发货按钮
    __chakan = (By.XPATH, "//a[text()='查看']") # 订单界面 查看订单信息按钮
    __freight = (By.XPATH, "//input[@value='发货']")  # 订单界面 发货按钮



    """
    封装页面操作
    """
    def complete_order_flow(self):
        self.click(self.__check_order)
        self.click(self.__pay_control)
        self.send_keys(self.__operation_note,"已付款")
        self.click(self.__submit_control)
        self.click(self.__distribution)
        self.click(self.__create_fahuo)
        self.click(self.__confirm)
        self.click(self.__go_fahuo)
        self.click(self.__chakan)
        self.click(self.__freight)

