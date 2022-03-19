# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/3 11:03
@作者 ： 王齐涛
@文件名称： 11111.py 
'''

# python中使用id()函数查看数据的内存地址
a = "100000"
b = "100000"

print(a)
print(b)

print(id(100),id(100))
print(id(-5),id(-5))
print(id(-6),id(-6))