# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/6 12:55
@作者 ： 王齐涛
@文件名称： read_element.py 
'''
import os
import yaml
from common.all_paths import ELEMENT_PATH


class Element(object):
    def __init__(self, name):
        self.file_name = name + ".yaml" or name + ".yml"
        self.element_path = os.path.join(ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError(f"{self.file_name}文件不存在")
        with open(self.element_path, encoding="utf-8", mode="r") as f:
            self.data = yaml.safe_load(stream=f)

    def __getitem__(self, item):
        # 如果在类中定义了__getitem__()方法，那么他的实例对象（假设为P）就可以这样P[key]取值。当实例对象做P[key]运算时，就会调用类中的__getitem__()方法。
        data = self.data.get(item)  # 类似于通过key获得value
        if data:
            name, value = data.split("==")  # 字符串切割
            return name, value
        raise ArithmeticError(f"{self.file_name}中不存在关键字{item}")