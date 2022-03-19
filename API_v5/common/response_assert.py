# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/8 22:21
@作者 ： 王齐涛
@文件名称： response_assert_v1.py
'''
import json
from common.logger_handler import GetLogger


class ResponseAssert:

    def __init__(self):
        self.log = GetLogger()

    def assert_status(self, except_code, actual_code):
        """
        响应状态码断言
        :param except_code: 预期结果
        :param actual_code: 实际结果
        :return:
        """
        try:
            assert except_code == actual_code
            return self.log.debug(f"断言检查点：预期结果{except_code}，实际结果{actual_code}"),\
                   self.log.debug("【测试结果：成功】")
        except:
            self.log.error(f"断言检查点：预期结果{except_code}，实际结果{actual_code}")
            self.log.error("【测试结果：失败】")

    def assert_body(self, except_body, actual_body):
        """
        响应头部字段断言
        :param except_code: 预期结果
        :param actual_code: 实际结果
        :return:
        """
        try:
            assert except_body == actual_body
            return self.log.debug(f"断言检查点：预期结果{except_body}，实际结果{actual_body}"),\
                   self.log.debug("【测试结果：成功】")
        except:
            self.log.error(f"断言检查点：预期结果{except_body}，实际结果{actual_body}")
            self.log.error("【测试结果：失败】")


    def assert_message(self, except_message, actual_message):
        """
        响应信息断言
        :param except_code: 预期结果
        :param actual_code: 实际结果
        :return:
        """
        try:
            text = json.dumps(actual_message, ensure_ascii=False)  #json.dumps 序列化时对中文默认使用的ascii编码, 想输出真正的中文需要指定ensure_ascii=False
            assert except_message in text
            return self.log.debug(f"断言检查点：预期结果{except_message}，实际结果{actual_message}"),\
                   self.log.debug("【测试结果：成功】")
        except:
            self.log.error(f"断言检查点：预期结果{except_message}，实际结果{actual_message}")
            self.log.error("【测试结果：失败】")

    def assert_time(self, except_time, actual_time):
        """
        响应头部字段断言
        :param except_code: 预期结果
        :param actual_code: 实际结果
        :return:
        """
        try:
            assert except_time < actual_time
            return self.log.debug(f"断言检查点：预期结果{except_time}，实际结果{actual_time}"),\
                   self.log.debug("【测试结果：成功】")
        except:
            self.log.error(f"断言检查点：预期结果{except_time}，实际结果{actual_time}")
            self.log.error("【测试结果：失败】")