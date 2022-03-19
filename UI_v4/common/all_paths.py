# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 20:52
@作者:   王齐涛
@文件:   all_paths.py
这里是获取所有文件的目录路径，调用的时候直接调用变量就好了
"""
import os
# os.sep用法 python在Windows上,文件的路径分隔符是'\',在Linux上是'/'
# log_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),"logs"),"log.log")     #存放日志的位置，日志器再调用，不可删除
# path1 = os.path.basename(__file__)  #返回文件名
# path2 = os.path.abspath(__file__)       #返回当前文件路径
# path3 = os.path.dirname(__file__)   #获取当前文件的上级目录
# path4 = os.path.exists(__file__)    #路径存在True,不存在False
# path4 = os.path.dirname(__file__)
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# os.path.dirname(os.path.abspath(__file__))
# logs_path = os.getcwd()+r"\\log_data"
# print(os.getcwd())


# 封装变量路径
CURRENT = os.path.abspath(__file__)   # 当前文件绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace("/", r"\\")  # 当前所有目录的上级(当前路径的上上级)


# 相关路径
CONFIG_PATH = os.path.join(BASE_DIR,"config")
DATA_PATH = os.path.join(BASE_DIR,"data")
HTML_PATH = os.path.join(BASE_DIR,"html_report")
LOGS_PATH = os.path.join(BASE_DIR,"logs")
CASE_PATH = os.path.join(BASE_DIR,"testcase_py")
PTHOTOS_PATH = os.path.join(BASE_DIR,"photos")
ELEMENT_PATH = os.path.join(BASE_DIR, "page_element")






