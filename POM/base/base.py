from selenium.webdriver.support.wait import WebDriverWait
from Common.wait_time import wait_element

class Base:
    def __init__(self,driver):
        self.driver = driver

    #打开链接
    def get_url(self,url):
        self.driver.get(url)

    #定位元素 ，方法一，直接用匿名函数
    def find_elements(self,loc):
        element = WebDriverWait(self.driver, timeout=10).until(lambda x: x.find_element(*loc))
        return element
        # return self.driver.find_element(*loc)

    # 定位元素方法二，调用封装的方法
    def find_element(self,local_):
        element = wait_element(self.driver,*local_)
        return element

    # 点击
    def click_btn(self,loc):
        self.find_element(loc).click()

    # 输入
    def send_key(self,loc,txt):
        self.find_element(loc).send_keys(txt)

    # 清除
    def clear(self,loc):
        self.find_element(loc).clear()
