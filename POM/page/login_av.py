from Base.base import Base
from selenium.webdriver.common.by import By


class LoginAv(Base):
    url = 'https://test2022.anyviewer.com/login'
    user = (By.NAME,'email')
    pwd = (By.NAME,'password')
    btn = (By.ID,'login')

    def login(self,name,pwd):
        self.get_url(self.url)
        self.clear(self.user)
        self.send_key(self.user,name)
        self.clear(self.pwd)
        self.send_key(self.pwd,pwd)
        self.click_btn(self.btn)