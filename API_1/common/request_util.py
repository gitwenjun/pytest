import json
import re
import jsonpath

import requests
from common.log_handler import logger
from common.yaml_handler import YamlHandler


class RequestUtil:
    def __init__(self,obj):
        self.obj = obj

    def replace_value(self,data):
        if data:
            # 保存数据类型
            data_type = type(data)
            # 判断数据类型转换为str
            if isinstance(data,dict) or isinstance(data,list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            for cs in range(1,str_data.count('${')+1):
                logger.debug(f"循环读取的数据：{cs}")
                # 替换
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}")
                    old_value = str_data[start_index:end_index+1]
                    logger.debug(f"原来的值为：{old_value}")
                    # 反射：通过类的对象和方法字符串调用方法
                    func_name = old_value[2:old_value.index('(')]
                    args_value1 = old_value[old_value.index('(')+1:old_value.index(')')]
                    new_value = ""
                    if args_value1 != "":
                        args_value2 = args_value1.split(',')
                        new_value = getattr(self.obj,func_name)(*args_value2)
                        logger.debug(f"替换后的值为：{new_value}")
                    else:
                        new_value = getattr(self.obj,func_name)
                        logger.debug(f"替换后的值为：{new_value}")
                    str_data = str_data.replace(old_value,str(new_value))
            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        logger.debug(f"最终的值为：{data}")
        return data

    session = requests.session()

    # 封装统一请求
    def send_request(self,url,method,**kwargs):
        method = str(method).lower()
        for key, value in kwargs.items():
            if key in ['headers','params','data','json']:
                kwargs[key] = self.replace_value(value)
            elif key == "files":
                for file_key, file_path in value.items():
                    value[file_key] = open(file_path,'rb')
        logger.debug(f"最终method值为：{method}")
        logger.debug(f"最终的url值为：{url}")
        logger.debug(f"最终的**kw值为：{kwargs}")
        # res = RequestUtil.session.request(url,method,**kwargs)
        res = requests.request(url, method, **kwargs)
        return res

    # 规范yaml测试用例
    def stand_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
            request_keys = caseinfo["request"].keys()
            if "method" in request_keys and "url" in request_keys:
                print("yaml基本架构检查通过")
                method = caseinfo["request"].pop("method")
                url = caseinfo["request"].pop("url")
                ressult = self.send_request(url=url,method=method,**caseinfo["request"])
                ressult_txt = ressult.txt
                ressult_code = ressult.status_code
                ressult_json = ""
                try:
                    ressult_json = ressult.json()
                    logger.debug(f"请求结果为：{ressult_json}")
                except Exception as e:
                    print("请求返回的不是json格式")
                if "extract" in caseinfo.keys():
                    for key,value in caseinfo.items():
                        if "(.*?)" in value or "(.+?)" in value:
                            re_value = re.search(value,ressult_txt)
                            if re_value:
                                extract_value = {key:re_value.group(1)}
                                YamlHandler().write_extract_yaml(extract_value)
                        else:
                            js_value = jsonpath.jsonpath(ressult_json,value)
                            if js_value:
                                extract_value = {key:js_value[0]}
                                YamlHandler().write_extract_yaml(extract_value)

            else:
                print("request中必须包含method,url")
        else:
            print("测试用例一级关键字中必须包含name,request,validate")





if __name__ == '__main__':
    # data = YamlHandler().read_yaml("../data/query_test.yaml")
    # logger.debug(f"初始值为：{data}")
    # RequestUtil(YamlHandler()).replace_value(data)

    data = YamlHandler().read_yaml("../data/login_test.yaml")[0]
    data = data["request"]
    logger.debug(f"初始值为：{data}")
    # RequestUtil(YamlHandler()).stand_yaml(data)
