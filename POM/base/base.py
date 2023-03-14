from Common.wait_time import wait_element,wait_elements
from selenium import webdriver

class Base:
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)

    def find_element(self,local):
        return wait_element(self.driver,*local)

    def find_elements(self,local):
        return wait_elements(self.driver,*local)

    def click_but(self,local):
        self.find_element(local).click()

    def send_keys(self,local,txt):
        self.find_element(local).send_keys(txt)

    def clear(self,local):
        self.find_element(local).clear()