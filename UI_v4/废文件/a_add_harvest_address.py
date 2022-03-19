# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/28 20:07
@作者 ： 王齐涛
@文件名称： a_add_harvest_address.py
'''
from page.Base import Base
from data.global_variable import *


class AddHarvestAddressPage(Base):
    """
    封装定位元素
    """
    __province_name = (By.ID,"selProvinces_0")  #省
    __city_name = (By.ID,"selCities_0")  #市
    __district_name = (By.ID,"selDistricts_0") #区
    __consignee_people_name = (By.ID,"consignee_0") #收货人姓名
    __consignee_people_site = (By.ID,"address_0") #地址
    __consignee_people_phone = (By.ID,"tel_0") #电话
    __consignee_people_email = (By.ID, "email_1")  # 电话
    __dispatching_control = (By.XPATH,"//input[@value='新增收货地址']")



    """
    封装页面操作
    """
    # @staticmethod
    def add_harvest_address(self):
        """
        添加用户的收获地址
        :return:
        """
        self.select(self.__province_name, "text", "北京")
        self.select(self.__city_name, "text", "北京")
        self.select(self.__district_name, "text", "东城区")
        self.send_keys(self.__consignee_people_name, consignee_people_name)
        self.send_keys(self.__consignee_people_site, consignee_people_site)
        self.send_keys(self.__consignee_people_phone, consignee_people_phone)
        self.send_keys(self.__consignee_people_email, consignee_people_email)
        self.click(self.__dispatching_control)



