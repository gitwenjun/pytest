# -*- encoding: utf-8 -*-
"""
@时间:   2021/12/5 20:12
@作者:   王齐涛
@文件:   element_type.py 
"""
from selenium.webdriver.common.by import By


LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}