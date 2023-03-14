from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from common.log_handler import logger


class Base:

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, loc):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(loc))
        # return self.driver.find_element(*loc)

    def find_elements(self, loc):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def send_keys(self, loc, txt):
        self.find_element(loc).send_keys(txt)

    def clean_send(self, loc):
        self.find_element(loc).clear()

    def bower_refresh(self):
        self.driver.refresh()

    def bower_back(self):
        self.driver.back()

    def bower_forward(self):
        self.driver.forward()

    def quit_driver(self):
        self.driver.quit()

    # 关闭当前窗口
    def close_driver(self):
        self.driver.close()

    # 切换上一窗口
    def switch_old_wind(self):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[0])

    # 切换新窗口
    def switch_new_wind(self):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])

    # 切换框架
    def switch_frame(self,loc):
        # 找到iframe元素再切换
        iframe1 = self.find_element(loc)
        self.driver.switch_to.frame(iframe1)

    # 切换回主界面
    def switch_default_wind(self):
        self.driver.switch_to.default_content()

    # 弹窗
    def switch_alter_(self):
        # self.driver.switch_to.alert.dismiss()
        self.driver.switch_to.alert.accept()
        # self.driver.switch_to.alert.send_keys("txt")
        # self.driver.switch_to.alert.text

    # 执行JS
    def execute_script(self, js):
        self.driver.execute_script(js)

    #下拉列表
    def select(self, loca, methon, data):
        option = Select(self.find_element(loca))
        if methon == "all":
            return option.all_selected_options
        elif methon == "index":
            print("------------index--------")
            option.select_by_index(f"{data}")
        elif methon == "value":
            option.select_by_value(f"{data}")
        elif methon == "text":
            option.select_by_visible_text(f"{data}")
        else:
            print("输入错误")


if __name__ == '__main__':
    url = "https://letcode.in/dropdowns"
    name = (By.ID, "fruits")
    # btu = (By.CSS_SELECTOR, "div>button[type='submit']")
    Ba = Base()
    Ba.open_url(url)
    Ba.select(name,"value",1)
    sleep(5)
