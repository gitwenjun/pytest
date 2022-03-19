# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/13 23:16
@作者:   王齐涛
@文件:   file_size.py
"""
# 1MB=1024KB=1024B*1024=1048576B
import os
from datetime import datetime

# path = "./2021-11-14-all.log"
# print(os.path.getsize(path))
#
#
# now_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
# print(now_time)



s = os.sep   # 类似于 \
root = r"G:\Python_code\Interface_Automation_v2\testcase_yaml"


def get_all_case():
    for i in os.listdir(root):  # os.listdir()：返回一个列表，其中包含有指定路径下的目录和文件的名称
        if os.path.isfile(os.path.join(root, i)):  # isfile判断某一对象(需提供绝对路径)是否为文件
            if i.startswith("test"):         # 来判断当前字符串是否是以另外一个给定的子字符串“开头”的
                print(i.split(".")[0])


#
# if __name__ == '__main__':
#     get_all_case()