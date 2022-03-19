# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/24 22:54
@作者 ： 王齐涛
@文件名称： 111.py 
'''
import os
import time
from datetime import datetime

from common.all_paths import CONFIG_PATH
from common.get_url import get_url

# url = "http://192.168.4.115"
# print(url)
# url1 = get_url("DEV_HTTP","http")
# print(url1)


# start = datetime.now()
# end = datetime.now()
# print(start)
# print(end)
# print((start - end).seconds)   # seconds忽略天 只看时分秒
#
# a=(1,2)
# print(a[1])
#
# bb=os.path.join("qqqq","3333")
# print(bb)
#
# path = CONFIG_PATH+"http_data.ini"
# print(path)

home = os.environ['LOGONSERVER']
home1 = os.environ['HOMEPATH']
print(home1)

def test01():
    key, value=('name', 'username')
    return key ,value


print(test01())