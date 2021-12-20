from time import sleep

import pytest
from selenium import webdriver
from Page.login_av import LoginAv
from Common.yaml_av import load_yaml

class Test_login:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.lg = LoginAv(self.driver)

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize('udata',load_yaml('../Date/yaml_login.yaml'))
    def test_login_01(self,udata):
        self.lg.login(udata['name'],udata['pwd'])
        assert udata['asserts']

if __name__ == '__main__':
    pytest.main(['-s'])