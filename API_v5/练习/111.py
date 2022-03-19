# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/9 12:20
@作者 ： 王齐涛
@文件名称： 111.py 
'''
import json

import yaml

from common.all_paths import CASE_PATH
from common.read_yaml import ReadYaml
from string import Template
# data = ReadYaml().read_yaml(CASE_PATH + r"\\get")
# print(data)

with open("get.yaml",encoding="utf-8") as f:
    data1 = f.read()
    # print(f"修改前{data1}")
    tem = Template(data1)
    # c = tem.substitute({"user":"wqt123456","paw":"wqt123456"})        # 方法一（ $value ）  必须都要输入才能匹配
    # print(f"修改后{c}")
    c1 = tem.safe_substitute({"pwd":"wqt123456"})       # 方法二 ( ${value} )  可以忽略匹配不到的变量
    print(c1)
    print(type(c1))



# with open("get.yaml",encoding="utf-8") as f:
#     data1= yaml.load(stream=f, Loader=yaml.FullLoader)
#     print(str(data1))
#     tem1 = Template(str(data1))
#     print(type(tem1))
#     c1 = tem1.safe_substitute(user="wqr123",pwd="wqt123456")       # 方法二 ( ${value} )  可以忽略匹配不到的变量
#     print(c1)


# s =Template('There are ${howmany} ${lang} Quotation Symbols')  #声明模板
# print(s.substitute(lang='Python', howmany=3))

# def test01():
#     a=1
#     b=2
#     c=3
#     return a,b,c
# a,b,c = test01()
# print(a)