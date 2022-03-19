# -*- encoding: utf-8 -*-
"""
@时间:   2021/12/5 22:00
@作者:   王齐涛
@文件:   timer.py
"""
from datetime import datetime


def coast_time(func):
    def fun(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"完成！用时{(start - end).seconds}秒")
        return result
    return fun