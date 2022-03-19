# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/15 16:57
@作者 ： 王齐涛
@文件名称： front_end_login.py
'''
from page.Base import Base


class FrontEndLoginPage(Base):
    """
    封装定位元素
    """
    url = Base.url

    __Submit = ("xpath", "//a[text()='登录']")
    __Login_input_name = ("name", "username")
    __Login_input_pw = ("name", "password")
    __Login_input_submit = ("name", "submit")




    """
    封装页面操作
    """
    def front_end_login(self,user_un,user_pw):
        """
        前端-登录
        :param user_un:
        :param user_pw:
        :return:
        """
        # try:
        #     self.find_element((By.XPATH, f"//font[text()='{user_un}']"))
        #     return "用户没有登录"
        # except:
        self.open_url()
        self.click(self.__Submit)
        self.send_keys(self.__Login_input_name,user_un)
        self.send_keys(self.__Login_input_pw,user_pw)
        self.click(self.__Login_input_submit)



