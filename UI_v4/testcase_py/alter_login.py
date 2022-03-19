# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/27 13:30
@作者:   王齐涛
@文件:   alter_login.py 
"""
import allure
import pytest

from 废文件.b_after_end_login import AfterEndLogin

data=[
    ("admin","wqt123456","正确的用户名和密码"),
    ("admin123","wqt123456","错误的用户名和正确的密码"),
    ("admin","wqt1234567890","正确的用户名和错误的密码")
]

@allure.story("分别传值")
@allure.title("登录测试用例-{title}")
@pytest.mark.parametrize("un,pw,title",data)
@pytest.mark.skip("暂时不测这条用例")
def test_login(home_page,un,pw,title):
    AfterEndLogin(home_page).after_end_login(admin_un=un,admin_pw=pw)


if __name__ == '__main__':
    pytest.main(["-s","alter_login.py"])