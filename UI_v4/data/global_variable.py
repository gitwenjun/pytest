# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/23 21:51
@作者 ： 王齐涛
@文件名称： global_variable.py
'''
from faker import Faker
import random


# 方法
from selenium.webdriver.common.by import By

fake = Faker(locale="zh_CN")
number = random.randint(1, 10000)

number_user = round(random.random(),3)


# 前端
serch_goods_name = "葫芦娃"     # 前端普通搜索商品名称


# 前端添加收获底地址
consignee_people_name = fake.name()                #添加收货人的姓名
consignee_people_phone = fake.phone_number()       #添加收货人的电话
consignee_people_email = fake.email()              #添加收货人的邮箱
consignee_people_site = fake.address()             #添加收货人的详细住址


# 前端注册账号
re_user_name = fake.user_name()
re_email = fake.email()
re_password = "wqt123456"
re_affirm_password = "wqt123456"
re_msn = fake.email()
re_qq = fake.ean8()
re_work_phone = fake.phone_number()
re_home_phone = fake.phone_number()
re_mobile_phone = fake.phone_number()
# re_password_prompt =    在函数中已定义
re_password_prompt_answer = "草莓"


# 后端添加商品
input_new_goods_name = "黄桃" + f"{number}"          # 商品名称
input_goods_classify_name = "男装"                   # 商品分类（写分类列表中有的，尽量写系统自带的一级分类名称）
input_goods_many_number = 1000                      # 商品售价
input_goods_weight_number = 20                      # 商品重量
input_goods_inventory_number = 2000                 # 商品库存


# 后端一级菜单栏
goods_manage = (By.XPATH, "//li[@key='02_cat_and_goods']")  # 商品管理
order_manage = (By.XPATH, "//li[@key='04_order']")          # 订单管理