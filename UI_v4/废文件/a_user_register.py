# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/16 10:43
@作者 ： 王齐涛
@文件名称： a_user_register.py
'''

from page.Base import Base


#随机名称变量
from data.global_variable import *

number_user = round(random.random(),3)
number_email = random.randint(1,90000)


class UserRegisterPage(Base):
    """
    封装定位元素
    """
    # url = Base.url + "/user.php?act=register"
    url = Base.url
    __sign_in_control = (By.XPATH, "//a[text()='注册']")  # 注册按钮
    __sign_in_username = (By.NAME, "username")
    __sign_in_email = (By.ID, "email")
    __sign_in_password = (By.NAME, "password")
    __sign_in_affirm_password = (By.NAME, "confirm_password")
    __sign_in_MSN = (By.NAME, "extend_field1")
    __sign_in_QQ = (By.NAME, "extend_field2")
    __sign_in_work_phone = (By.NAME, "extend_field3")
    __sign_in_home_phone = (By.NAME, "extend_field4")
    __sign_in_mobile_phone = (By.NAME, "extend_field5")
    __select_hint = (By.NAME, "sel_question")
    __sign_in_passwd_answer = (By.NAME, "passwd_answer")
    __at_once_sign_in = (By.CLASS_NAME, "us_Submit_reg")
    __gain_succeed_text = (By.XPATH,f"//p[text()='用户名 {re_user_name} 注册成功']")   # 获取注册成功的文本信息


    """
    封装页面操作
    """
    def user_register(self):
        """
        用户注册
        :return:
        """
        self.open_url()
        self.click(self.__sign_in_control)
        self.send_keys(self.__sign_in_username, re_user_name)
        self.send_keys(self.__sign_in_email, re_email)
        self.send_keys(self.__sign_in_password, re_password)
        self.send_keys(self.__sign_in_affirm_password, re_affirm_password)
        self.send_keys(self.__sign_in_MSN, re_msn)
        self.send_keys(self.__sign_in_QQ, re_qq)
        self.send_keys(self.__sign_in_work_phone, re_work_phone)
        self.send_keys(self.__sign_in_home_phone, re_home_phone)
        self.send_keys(self.__sign_in_mobile_phone, re_mobile_phone)
        self.select(self.__select_hint,"text","我最喜爱的食物？")
        self.send_keys(self.__sign_in_passwd_answer, re_password_prompt_answer)
        self.screenshot("前端注册界面_注册信息详情截图")
        self.click(self.__at_once_sign_in)
        text = self.gain(self.__gain_succeed_text)
        return text




