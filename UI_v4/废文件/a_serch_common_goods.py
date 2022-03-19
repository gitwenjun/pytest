# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/28 18:54
@作者 ： 王齐涛
@文件名称： a_serch_common_goods.py
'''
from selenium.webdriver.common.by import By
from page.Base import Base


class SerchCommonGoodsPage(Base):
    """
    封装定位元素
    """
    url = Base.url+"/index.php"

    # 搜索商品
    search_goods_input_box = (By.XPATH, "//input[@name='keywords']")  # 搜索输入框
    search_control = (By.XPATH, "//input[@name='imageField']")  # 搜索按钮
    buy_goods = (By.XPATH,"//img[@src='themes/ecmoban_meilishuo/images/goumai2.gif']")  # 立即购买


    # 我的账户
    my_account_control = (By.LINK_TEXT, "我的账户")




    """
    封装页面操作
    """
    def serch_common_goods(self, name="请输入搜索名称"):
        """
        普通搜索商品（只需要输入商品的名称就可以）
        :param name:
        :return:
        """
        click_goods = (By.XPATH, f"//div[@class='goodsItem']//a[text()='{name}']")
        self.open_url()
        self.send_keys(self.search_goods_input_box,name)  # 搜索商品输入框
        self.click(self.search_control)  # 点击”搜索“按钮
        self.click(click_goods)
        self.click(self.buy_goods)


    def my_account(self):
        """
        点击我的账户（进入用户中心）
        :return:
        """
        self.click(self.my_account_control)



