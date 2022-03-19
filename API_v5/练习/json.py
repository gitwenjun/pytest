# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/3 12:43
@作者 ： 王齐涛
@文件名称： json.py 
'''
# import json
#
# def loads(data):
#     """
#     反序列化    json对象->python数据类型(dict)
#     :param content:
#     :return:
#     """
#     return json.loads(data)
#
#
# def dumps(data):
#     """
#     序列化     python数据类型->json对象
#     :param data:
#     :return:
#     """
#     # ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文
#     return json.dumps(data, ensure_ascii=True, encoding="utf-8")
#
#
# def is_string_json(string):
#     """
#     判断传入的字符串是否为json格式,非字典类型的字符串会报错
#     :param string:
#     :return:
#     """
#     try:
#         json.loads(string)
#         return True
#     except:
#         return False