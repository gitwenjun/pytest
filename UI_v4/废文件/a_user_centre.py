# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 18:56
@作者 ： 王齐涛
@文件名称： a_user_centre.py 
'''
from selenium.webdriver.common.by import By

from page.Base import Base


class UserCentrePage(Base):
    """
    封装定位元素
    """
    url = Base.url + "/user.php"
    __my_order = (By.XPATH, "//img[@src='themes/ecmoban_meilishuo/images/u3.gif']")   # 我的订单




    """
    封装页面操作
    """
    def operate_order(self,order_number):
        self.open_url()
        self.click(self.__my_order) #点击我的订单
        self.click((By.XPATH, f"//a[text()='{order_number}']/../..//font[@class='f6']/a"))  # 操作订单的状态（一般是确认收货）
        self.pop_up_windows()   # 弹出确认的窗口，点击确认