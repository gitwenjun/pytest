from time import sleep

from selenium.webdriver.common.by import By
from base.base import Base


class LoginPage(Base):
    url = 'https://ticket.pescms.com/?m=Login&a=index'
    email = (By.NAME, 'email')
    password = (By.NAME, 'password')
    login_btu = (By.CSS_SELECTOR, '.am-btn')
    res = (By.CSS_SELECTOR, '.am-topbar')

    def login(self, email, pwd):
        self.open_url(self.url)
        self.send_keys(self.email, email)
        self.clean_send(self.password)
        self.send_keys(self.password, str(pwd))
        self.click_element(self.login_btu)
        sleep(3)

    def result(self):
        return self.find_element(self.res)


