# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/29 10:45
@作者 ： 王齐涛
@文件名称： b_add_goods.py
'''

from page.Base import Base

# 随机变量
from data.global_variable import *


class AddGoodsPage(Base):
    """
    封装定位元素
    """
    # 后端-商品管理-添加新商品
    goods_name_contorl = ("xpath", "//input[@name='goods_name']")  # 添加新商品名称
    __select_element = (By.XPATH,"//select[@onchange='hideCatDiv()']") # 下拉框
    add_goods_classify_contorl = ("xpath", "//a[text()='添加分类']")  # 添加商品分类
    input_goods_classify_name_contorl = ("xpath", "//input[@name='addedCategoryName']")  # 输入商品分类名称
    confirm_goods_classify_contorl = ("xpath", "//span[@id='category_add']/a[1]")  # 确认商品分类
    goods_classify_contorl = ("xpath", "//select[@name='cat_id']")  # 选择新商品分类
    our_store_many_contorl = ("xpath", "//input[@name='shop_price']")  # 添加新商品本店售价
    else_data_contorl = ("xpath", "//span[text()='其他信息']")  # 点击其他信息
    goods_weight_contorl = ("xpath", "//input[@name='goods_weight']")  # 添加商品的重量
    goods_inventory_contorl = ("xpath", "//input[@name='goods_number']")  # 添加商品的库存数量
    __get_text = (By.XPATH,"//td[@style='font-size: 14px; font-weight: bold']")  # 获取添加成功后的文本
    __upload_file = (By.XPATH, "//input[@name='goods_img']")    # 上传文件



    """
    封装页面操作
    """
    def add_goods(self):
        """
        后端添加商品信息
        :return:
        """
        self.send_keys(self.goods_name_contorl,input_new_goods_name)  # 添加新商品名称,用变量代替
        self.select(self.__select_element, "text", input_goods_classify_name)

        # self.click(self.__select_element)
        # true = self.wait_visible_element((By.XPATH,f"//select[@onchange='hideCatDiv()']//option[text()='{input_goods_classify_name}']"))
        # if true == True:
        #     self.select(self.__select_element, "text", input_goods_classify_name)
        # else:
        #     self.click(self.add_goods_classify_contorl)
        #     self.send_keys(self.input_goods_classify_name_contorl,input_goods_classify_name)
        #     self.click(self.confirm_goods_classify_contorl)

        self.send_keys(self.our_store_many_contorl,input_goods_many_number)  # 新商品本店售价

        # self.upload_files(self.__upload_file, r"G:\\suoluetu\\aa.jpg")   # 上传图片

        self.click(self.else_data_contorl) # 点击其他信息
        self.send_keys(self.goods_weight_contorl,input_goods_weight_number)  # 商品重量
        self.send_keys(self.goods_inventory_contorl,input_goods_inventory_number)  # 商品存库数量
        self.click(("xpath", "//input[@value=' 确定 ']"))
        succeed_text = self.gain(self.__get_text)
        return input_new_goods_name,succeed_text

