# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/3 12:29
@作者 ： 王齐涛
@文件名称： get_case.py 
'''
import os

root = r"G:\Python_code\Interface_Automation_v2\testcase_yaml"
def get_all_case():
    for i in os.listdir(root):  # os.listdir()：返回一个列表，其中包含有指定路径下的目录和文件的名称
        if os.path.isfile(os.path.join(root, i)):  # isfile判断某一对象(需提供绝对路径)是否为文件
            if i.startswith("test"):         # 来判断当前字符串是否是以另外一个给定的子字符串“开头”的
                print(i.split(".")[0])


if __name__ == '__main__':
    get_all_case()