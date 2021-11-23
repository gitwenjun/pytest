from selenium.webdriver.common.by import By

# 页面元素类
class BingPage():
    def __init__(self, driver):
        self.driver = driver

    def input_box(self):
       return self.driver.find_element(By.ID,value='sb_form_q')

    def ck_box(self):
        return self.driver.find_element(By.ID,value='search_icon')

# 页面操作类
class BingOper():
    def __init__(self,driver):
        self.oper = BingPage(driver)

    # 搜索框输入
    def input_box(self,msg):
        self.oper.input_box().clear()
        self.oper.input_box().send_keys(msg)

    def ck_box(self):
        self.oper.ck_box().click()


# 业务逻辑类
class BingBus():
    def __init__(self,driver):
        self.bing_bus = BingOper(driver)

    def bing_b(self,msg):
        self.bing_bus.input_box(msg)
        self.bing_bus.ck_box()