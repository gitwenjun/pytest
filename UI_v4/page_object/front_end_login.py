# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/3 22:45
@作者 ： 王齐涛
@文件名称： front_end_login.py
'''
from selenium import webdriver
from common.read_element import Element
from page.Base import Base

login = Element("front_login")

print(login["登录按钮"])
class FrontEndLogin(Base):

    url = Base.url

    def test01(self):
        self.open_url()
        self.send_keys(login["用户名"],"wqt123@qq.com")
        self.send_keys(login["密码"], "wqtwan123")
        self.click(login["登录按钮"])




