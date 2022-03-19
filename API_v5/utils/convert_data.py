# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/12/9 23:20
@作者 ： 王齐涛
@文件名称： convert_data.py 
'''
from string import Template
import yaml
from common.logger_handler import GetLogger

log = GetLogger()


class ConvertData:

    @staticmethod
    def convert_data_text(args, ele):
        """
        读取参数的方法来实现数据替换
        :param args: 传入的参数是dict
        :param ele:
        :return:
        """
        log.debug("这里需要参数的替换，修改内容如下")
        log.debug(f"修改前参数：{args}")
        tem = Template(str(args))
        alter_data = tem.safe_substitute(ele)       # 方法二( ${value} )可以忽略匹配不到的变量 ,字符串模板的安全替换(safe_substitute) 详解
        log.debug(f"修改后参数：{alter_data}")
        return eval(alter_data)        # 将str转为dict

    @staticmethod
    def convert_data_dict(filename, ele):
        """
        读取yaml文件的方法来实现数据替换,返回的结果是dict
        :param filename: 用例文件名
        :param ele: 传入的类型是dict,比如{"goods_number": "150","haha":"120"}
        :return:
        """
        with open(filename+".yaml", encoding="utf-8") as f:
            front_data= yaml.load(stream=f, Loader=yaml.FullLoader)
            print(f"修改前{str(front_data)}")
            tem = Template(str(front_data))
            alter_data = tem.safe_substitute(ele)       # 方法二( ${value} )可以忽略匹配不到的变量
            print(f"修改后{alter_data}")

    @staticmethod
    def convert_data_str(filename, ele):
        """
        读取普通文件的方法来实现数据替换，返回的结果是str
        :param filename:
        :param ele:
        :return:
        """
        with open(filename+".yaml", encoding="utf-8") as f:
            front_data = f.read()
            print(f"修改前{front_data}")
            tem = Template(front_data)
            alter_data = tem.substitute(ele)        # 方法一( $value )必须都要输入才能匹配
            print(f"修改后{alter_data}")




if __name__ == '__main__':
    aa ={'name': '测试用例1：进入商品ID为134的页面', 'request': {'method': 'post', 'url': '/goods', 'params': {'goods_id': '${goods_number}', 'goods': '$haha', 'session': None}}, 'assert': [{'equals': {'status_code': 200}}, {'equals': {'succeed': 1}}]}
    ConvertData.convert_data_text(aa,{"goods_number": "150","haha":"120"})