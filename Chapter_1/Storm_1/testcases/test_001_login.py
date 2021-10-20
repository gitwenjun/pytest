from selenium import webdriver
import pytest
from Chapter_1.Storm_1.pageobject import login_page
from Chapter_1.Data.parse_csv import parses_csv

data = parses_csv('../Data/login_csv_1.csv')
print(data)
@pytest.mark.parametrize(('username', 'pwd', 'status'), data)
class TestLogin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('http://wenjunblog.cn/wp-login.php?loggedout=true&wp_lang=zh_CN')

    def teardown(self):
        self.driver.quit()

    def test_001_login(self,username,pwd,status):
        login_page.LoginScenario(self.driver).login(username, pwd)
        if status == '0':
            # 登录失败的信息
            text = login_page.LoginOper(self.driver).get_login_fild_info()
            print(text)
            assert '错误' in text
        elif status == '1':
            text = login_page.LoginOper(self.driver).get_login_name()
            assert username in text
            assert '文章' in self.driver.page_source
        else:
            print('参数化的状态只能传入0或1')

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir=./report'])
