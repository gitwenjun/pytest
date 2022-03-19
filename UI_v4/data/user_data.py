# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 22:24
@作者 ： 王齐涛
@文件名称： user_data.py 
'''

from common.get_url import get_url


# 前端登录测试相关数据
front_url = get_url("DEV_HTTP","http")
front_un = "wqt123456"
front_pw = "wqt123456"


# 后端登录相关测试数据
after_url = front_url + "/admin"
after_un = "admin"
after_pw = "wqt123456"
