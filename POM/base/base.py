

class Base:
    def __init__(self,driver):
        self.driver = driver

    #打开链接
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def find_element(self,loc):
        return self.driver.find_element(*loc)

    #点击
    def click_btn(self,loc):
        self.find_element(loc).click()

     #输入
    def send_key(self,loc,txt):
        self.find_element(loc).send_keys(txt)

    #清除
    def clear(self,loc):
        self.find_element(loc).clear()
