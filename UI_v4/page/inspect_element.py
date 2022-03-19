# -*- encoding: utf-8 -*-
"""
@时间:   2021/12/5 20:21
@作者:   王齐涛
@文件:   inspect_element.py
"""
import os
import yaml
import time
from common.all_paths import ELEMENT_PATH
from config.element_type import LOCATE_MODE
from common.timer import coast_time


@coast_time
def insp_element():
    time.perf_counter()
    for files in os.listdir(ELEMENT_PATH):
        if files.startswith("front"):
            _path = os.path.join(ELEMENT_PATH,files)
            with open(_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
            for k in data.values():
                try:
                    key,value = k.split("==")
                    if key not in LOCATE_MODE:
                        raise Exception(f"文件{_path}中{key}类型没有封装")
                except:
                    raise Exception("文件{path}中 == 没写完整")
    else:
        print("执行完成，全部通过")

if __name__ == '__main__':
    insp_element()