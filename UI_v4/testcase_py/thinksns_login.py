# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/6 15:56
@作者 ： 王齐涛
@文件名称： thinksns_login.py 
'''
import pytest

from page_object.front_end_login import FrontEndLogin


class TestUserLogin:

    def test_c(self,home_page):
        """前端注册用户"""
        FrontEndLogin(home_page).test01()


if __name__ == '__main__':
    pytest.main(["-s","thinksns_login.py"])