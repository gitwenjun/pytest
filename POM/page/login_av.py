from Base.base import Base
from selenium.webdriver.common.by import By


class login_page(Base):

    url = "https://www.anyviewer.com/login.html"
    name = (By.NAME, 'email')
    pwd = (By.NAME, 'password')
    btn = (By.ID, 'login')
    asts = (By.CSS_SELECTOR, '.change-password')

    def login(self,name,pwd):
        self.open_url(self.url)
        self.send_keys(self.name,name)
        self.send_keys(self.pwd,pwd)
        self.click_but(self.btn)

    # 断言登录成功
    def ast(self):
        return self.find_element(self.asts)