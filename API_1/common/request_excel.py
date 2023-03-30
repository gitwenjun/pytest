import json
import re
import jsonpath

import requests

from common.excel_operate import ExcelOperate
from common.log_handler import logger
from common.request_util import RequestUtil
from common.yaml_handler import YamlHandler


class ExcelRequestUtil:
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
                # logger.debug(f"循环读取次数：{cs}")
                # 替换
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}")
                    old_value = str_data[start_index:end_index+1]
                    # logger.debug(f"原来的值为：{old_value}")
                    # 反射：通过类的对象和方法字符串调用方法
                    func_name = old_value[2:old_value.index('(')]
                    args_value1 = old_value[old_value.index('(')+1:old_value.index(')')]
                    new_value = ""
                    if args_value1 != "":
                        args_value2 = args_value1.split(',')
                        new_value = getattr(self.obj,func_name)(*args_value2)
                        # logger.debug(f"替换后的值为：{new_value}")
                    else:
                        new_value = getattr(self.obj,func_name)
                        # logger.debug(f"替换后的值为：{new_value}")
                    str_data = str_data.replace(old_value,str(new_value))
            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        # logger.debug(f"最终的值为：{data}")
        return data

    sess = requests.session()

    # 封装统一请求
    def send_request(self,title,url,method,headers=None,**kwargs):
        method = str(method).lower()
        for key, value in kwargs.items():
            if key in ['params', 'data', 'json']:
                kwargs[key] = self.replace_value(value)
            elif key == "files":
                for file_key, file_path in value.items():
                    value[file_key] = open(file_path, 'rb')

        logger.info(f"测试用例标题：{title}")
        logger.info(f"请求url：{url}")
        logger.info(f"请求方法：{method}")
        logger.info(f"请求头：{headers}")
        logger.info(f"请求参数：{kwargs}")
        res = ExcelRequestUtil.sess.request(method=method, url=url, headers=headers, **kwargs)
        # logger.debug(f"返回的res值为：{res.text}")
        return res

    # 断言
    def assert_result(self, yq_result, sj_result, return_code,result_wt,fileName):
        all_flag = 0
        yq_result = eval(yq_result)
        for yq in yq_result:
            for key, value in yq.items():
                if key == "equals":
                    flag = self.equals_assert(value, return_code, sj_result)
                    all_flag = all_flag + flag
                elif key == "contains":
                    flag = self.contains_assert(value, sj_result)
                    all_flag = all_flag + flag
                else:
                    print("暂不支持此断言")
        c, v = ExcelOperate(fileName).find_row_col_by_value(result_wt)
        if all_flag != 0:
            print(c, v)
            ExcelOperate(fileName).update_excel(c, v, "fail")
        assert all_flag == 0
        logger.info(f"断言成功，测试通过")
        ExcelOperate(fileName).update_excel(c, v, "pass")

    # 相等断言
    def equals_assert(self, values, return_code, sj_result):
        flag = 0
        for assert_key, assert_value in values.items():
            if assert_key == "status_code": # 断言状态码
                logger.info(f"【预期结果】：{assert_value},【实际结果】：{return_code}")
                if assert_value != return_code:
                    flag += 1
                    logger.error(f"断言失败，返回的状态码不等于{assert_value}")
            else:
                lists = jsonpath.jsonpath(sj_result,'$..%s' % assert_key)
                if lists:
                    logger.info(f"【预期结果】：{assert_value},【实际结果】：{lists}")
                    if assert_value not in lists:
                        flag += 1
                        logger.error(f"断言失败：{assert_key}不等于{assert_value}")
                else:
                    flag += 1
                    logger.error(f"断言失败：返回的结果中不包括{values}")
        return flag

    # 包含断言
    def contains_assert(self, value, sj_result):
        flag = 0
        logger.info(f"【预期结果】：{value},【实际结果】：{sj_result}")
        if value not in str(sj_result):
            flag += 1
            logger.error(f"断言失败：返回结果中不包含{value}")
        return flag

    # 规范yaml测试用例
    def stand_yaml(self, caseinfo, fileName):
        caseinfo_keys = caseinfo.keys()
        if "name" in caseinfo_keys and "validate" in caseinfo_keys:
            if "method" in caseinfo_keys and "url" in caseinfo_keys:
                print("yaml基本架构检查通过")
                title = caseinfo["name"]
                method = caseinfo["method"]
                url = caseinfo["url"]
                headers = caseinfo["headers"]
                data = eval(caseinfo["data"])
                ressult = self.send_request(title=title,url=url,method=method,headers=headers,**data)
                ressult_txt = ressult.text
                ressult_code = ressult.status_code
                ressult_json = ""
                try:
                    ressult_json = ressult.json()
                    logger.info(f"响应结果：{ressult_json}")
                except Exception as e:
                    print("请求返回的不是json格式")
                if "extract" in caseinfo.keys():
                    for key,value in eval(caseinfo["extract"]).items():
                        if "(.*?)" in value or "(.+?)" in value:
                            re_value = re.search(value,ressult_txt)
                            # logger.debug(f"正则表达式提取的值为：{re_value}")
                            if re_value:
                                extract_value = {key: re_value.group(1)}
                                YamlHandler().write_extract_yaml(extract_value)
                        else:
                            js_value = jsonpath.jsonpath(ressult_json,value)
                            # logger.debug(f"jsonpath表达式提取的值为：{js_value}")
                            if js_value:
                                extract_value = {key: js_value[0]}
                                YamlHandler().write_extract_yaml(extract_value)
                # 断言结果
                # print(caseinfo["validate"])
                self.assert_result(caseinfo["validate"], ressult_json, ressult_code,caseinfo["case_id"],fileName)

            else:
                print("request中必须包含method,url")
        else:
            print("测试用例一级关键字中必须包含name,validate")





if __name__ == '__main__':

    data = ExcelOperate("login_test.xls").read_excel()[0]
    # print(data)
    ExcelRequestUtil(YamlHandler()).stand_yaml(data)

    # data = YamlHandler().read_yaml("login_test.yaml")[0]
    # RequestUtil(YamlHandler()).stand_yaml(data)
