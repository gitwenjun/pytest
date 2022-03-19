# -*- encoding: utf-8 -*-
'''
@时间 ： 2021/11/8 22:21
@作者 ： 王齐涛
@文件名称： response_assert_v1.py
'''
from common.logger_handler import GetLogger

class Assert:

    def __init__(self):
        self.log = GetLogger()


    def assert_message(self, except_message, actual_message):
        """
        获取的文本信息断言
        :param except_code: 预期结果
        :param actual_code: 实际结果
        :return:
        """
        try:
            assert except_message in actual_message
            return self.log.debug(f"断言检查点--预期结果:{except_message}，实际结果:{actual_message}"),\
                   self.log.debug("【测试结果：断言成功】")
        except:
            self.log.error(f"断言检查点：预期结果{except_message}，实际结果{actual_message}")
            self.log.error("【测试结果：断言失败】")


