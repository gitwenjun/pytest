# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/26 11:21
@作者 ： 王齐涛
@文件名称： user_register.py 
'''
import allure
import pytest
from page.Base import Base
from 废文件.a_user_register import UserRegisterPage
from common.result_assert import Assert


class TestUserRegister:
    @pytest.mark.maoyan
    @allure.title("注册用户-输入所有正确的信息")
    @allure.feature("前端操作")
    def test_correct_required_parameter(self,home_page):
        """前端注册用户"""
        text = UserRegisterPage(home_page).user_register()
        path = Base(home_page).screenshot("前端注册界面_注册成功截图")
        file_png = open(path, mode='rb').read()     # 必须要加这个才能在allure展示完整的图片
        allure.attach(body=file_png, name="前端注册界面_注册成功截图",
                      attachment_type=allure.attachment_type.PNG)
        Assert().assert_message("注册成功", text)


if __name__ == '__main__':
    pytest.main(["-s","user_register.py"])