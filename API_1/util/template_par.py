from string import Template

import yaml

from common.log_handler import logger
from common.yaml_handler import YamlHandler


class Template_paramse:

    def replase_para(self, arg, data):
        logger.debug(f"替换前的参数：{arg}")
        temp = Template(str(arg)).safe_substitute(data)
        res = eval(temp)
        logger.debug(f"替换后的参数：{res}")
        # logger.debug(f"参数类型是 ：{type(temp)}")
        return res

    def replase_txt(self, fileName, data):
        with open(fileName, mode="r", encoding="utf-8") as f:
            temp = yaml.load(stream=f, Loader=yaml.FullLoader)
            logger.debug(f"替换前的参数：{temp}")
            tmp = Template(str(temp))
            res = tmp.safe_substitute(data)
            logger.debug(f"替换后的参数：{res}")

    def replace_dict(self, arg, data):
        data = Template(str(arg)).substitute(data)
        return yaml.safe_load(data)

    @staticmethod
    def convert_data_text(args, ele):
        """
        读取参数的方法来实现数据替换
        :param args: 传入的参数是dict
        :param ele:
        :return:
        """
        logger.debug("这里需要参数的替换，修改内容如下")
        logger.debug(f"修改前参数：{args}")
        tem = Template(str(args))
        alter_data = tem.safe_substitute(ele)  # 方法二( ${value} )可以忽略匹配不到的变量 ,字符串模板的安全替换(safe_substitute) 详解
        logger.debug(f"修改后参数：{alter_data}")
        return eval(alter_data)  # 将str转为dict

if __name__ == '__main__':
    a = YamlHandler().read_yaml("../data/change_info.yaml")
    location = {"location": "广州"}
    cc = Template_paramse().replase_para(a,location)
    print(cc)