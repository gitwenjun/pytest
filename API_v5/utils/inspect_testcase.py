# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/7 19:14
@作者 ： 王齐涛
@文件名称： inspect_testcase.py 
'''
import os
import jsonpath
import yaml
from common.all_paths import CASE_PATH
from common.logger_handler import GetLogger
from common.times import running_time

log = GetLogger()


@running_time       # 时间装饰器，统计的是函数运行的时间
def insp_element():
    """该函数用于检查yaml文件中的用例参数是否正确"""
    for files in os.listdir(CASE_PATH):    # 返回一个由文件名和目录名组成的列表,列出路径下所有的文件
        if files.startswith("test"):    # 以test开头的yaml文件
            _path = os.path.join(CASE_PATH, files)   # 路径的拼接（拼接后是相对路径）
            log.info(f"测试的文件夹:{_path}")
            with open(_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)  # 返回的是一个列表，下面进行遍历
                for i in data:
                    log.debug(i)     # 打印每一条接口用例,每一条用例是dict类型
                    if "name" in i.keys() and "request" in i.keys() and "assert" in i.keys():   # 检查yaml文件中一级参数
                        if jsonpath.jsonpath(i, "$..url") and jsonpath.jsonpath(i, "$..method"):
                            log.debug("执行通过")
                        else:
                            log.error("二级目录格式有问题,必须包含字段：url，method...")
                    else:
                        log.error("一级目录格式有问题,必须包含字段：name，request，assert...")


if __name__ == '__main__':
    insp_element()