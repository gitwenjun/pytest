# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/28 20:07
@作者 ： 王齐涛
@文件名称： a_check_out.py
'''
from selenium.webdriver.common.by import By
from page.Base import Base


class CheckOutPage(Base):
    """
    封装定位元素
    """
    url = Base.url + "/flow.php?step=cart"
    __settle_accounts_contorl = (By.XPATH, "//img[@alt='checkout']")  # 结算中心
    __amend_number_input = (By.NAME,"goods_number[43]")   # 输入数量文本框
    __update_shopping_trolley = (By.XPATH, "//input[@value='更新购物车']")



    """
    封装页面操作
    """
    def colsing_centre(self):
        """
        结算中心
        :return:
        """
        self.open_url()
        self.click(self.__settle_accounts_contorl)


    def amend_number(self,number):
        """
        修改商品购买数量
        :return:
        """
        aa=self.clear(self.__amend_number_input)
        self.send_keys(aa,number)
        self.click(self.__update_shopping_trolley)



