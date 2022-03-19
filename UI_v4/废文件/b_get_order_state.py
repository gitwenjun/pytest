# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 17:53
@作者 ： 王齐涛
@文件名称： b_get_order_state.py 
'''
from selenium.webdriver.common.by import By

from page.Base import Base


class GetOrderStatePage(Base):
    """
    封装定位元素
    """
    __check_order_state = (By.XPATH,"//div[@class='list-div'][3]//tr[6]//td[3]//div")  # 查看订单状态
    __check_payment_state = (By.XPATH,"//div[@class='list-div'][3]//tr[6]//td[4]//div")  # 查看付款状态
    __check_shipments_state = (By.XPATH,"//div[@class='list-div'][3]//tr[6]//td[5]//div")  # 查看发货状态
    __buyer_state = (By.XPATH, "//*[text()='买家']//..//..//td[5]//div")  # 操作者为买家，获取发货状态的字段（正确显示：收货确认）



    """
    封装页面操作
    """
    def get_shipments_state(self,order_num):
        self.click((By.XPATH, f"//a[text()='{order_num}']"))
        txt = self.gain(self.__buyer_state)
        return txt