from Base.base import Base
from selenium.webdriver.common.by import By


class LoginAv(Base):
    url = 'https://www.anyviewer.com/login.html'
    user = (By.NAME,'email')
    pwd = (By.NAME,'password')
    btn = (By.ID,'login')
    asts = (By.CSS_SELECTOR,'.change-password')

    #登录流程
    def login(self,name,pwd):
        self.get_url(self.url)
        self.clear(self.user)
        self.send_key(self.user,name)
        self.clear(self.pwd)
        self.send_key(self.pwd,pwd)
        self.click_btn(self.btn)

    #断言登录成功
    def ast(self):
        return self.find_element(self.asts)