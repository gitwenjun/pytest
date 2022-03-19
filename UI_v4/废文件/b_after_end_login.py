# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/9/15 16:57
@作者 ： 王齐涛
@文件名称： front_end_login.py
'''

from page.Base import Base



class AfterEndLogin(Base):
    """
    封装定位元素
    """
    url = Base.url + "/admin/index.php"
    __Admin_input_name = ("name", "username")
    __Admin_input_pw = ("name", "password")
    __Admin_input_submit = ("css selector", "[value='进入管理中心']")



    """
    封装页面操作
    """
    def after_end_login(self,admin_un,admin_pw):
        """
        后端用户登录
        :param admin_un:
        :param admin_pw:
        :return:
        """
        # try:
        #     self.find_element((By.XPATH, f"//font[text()='{user_un}']"))
        #     return "用户没有登录"
        # except:
        self.open_url()
        self.send_keys(self.__Admin_input_name, admin_un)
        self.send_keys(self.__Admin_input_pw, admin_pw)
        self.click(self.__Admin_input_submit)




