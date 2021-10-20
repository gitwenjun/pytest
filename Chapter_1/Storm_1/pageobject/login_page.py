from Chapter_1.Storm_1.Common.Base_wait import Base
# 封装第一层  页面元素对象层
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # 登录名
    def find_name(self):
        # ele = self.driver.find_element_by_id('user_login')
        ele = Base(self.driver).get_element('id,user_login')
        return ele

    # 登录密码
    def find_pwd(self):
        # ele = self.driver.find_element_by_id('user_pass')
        ele = Base(self.driver).get_element('id,user_pass')
        return ele

    # 登录按钮
    def find_login_btn(self):
        # ele = self.driver.find_element_by_id('wp-submit')
        ele = Base(self.driver).get_element('id,wp-submit')
        return ele

    # 登录成功
    def find_login_name(self):
        # ele = self.driver.find_element_by_id('wp-admin-bar-my-account')
        ele = Base(self.driver).get_element('id,wp-admin-bar-my-account')
        return ele

    # 登录失败
    def find_login_failed(self):
        # ele = self.driver.find_element_by_id('login_error')
        ele = Base(self.driver).get_element('id,login_error')
        return ele


# 封装第二层 页面元素操作层
class LoginOper():
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    # 输入用户名
    def input_username(self,username):
        self.login_page.find_name().clear()
        self.login_page.find_name().send_keys(username)

    # 输入密码
    def input_pwd(self,pwd):
        self.login_page.find_pwd().clear()
        self.login_page.find_pwd().send_keys(pwd)

    # 点击登录
    def click_login_btn(self):
        self.login_page.find_login_btn().click()

    # 登录成功
    def get_login_name(self):
        return self.login_page.find_login_name().text

    # 登录失败
    def get_login_fild_info(self):
        return self.login_page.find_login_failed().text


# 封装第三层 页面业务场景层
class LoginScenario():

    def __init__(self, driver):
        self.login_oper = LoginOper(driver)

    def login(self, username, pwd):
        self.login_oper.input_username(username)
        self.login_oper.input_pwd(pwd)
        self.login_oper.click_login_btn()
