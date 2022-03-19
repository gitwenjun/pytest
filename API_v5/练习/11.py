# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/10 17:04
@作者 ： 王齐涛
@文件名称： 11.py 
'''
aa ={'name': '测试用例1：进入商品ID为134的页面', 'request': {'method': 'post', 'url': '/goods', 'params': {'goods_id': '${goods_number}', 'goods': '$haha', 'session': None}}, 'assert': [{'equals': {'status_code': 200}}, {'equals': {'succeed': 1}}]}
bb = {"goods_number": "150","haha":"120"}
print(type(aa))
print(aa["name"])